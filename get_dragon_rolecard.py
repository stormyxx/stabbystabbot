from dataclasses import dataclass
from typing import List, Tuple
import re
import hashlib

from flask_discord_interactions import Embed

from embeds import rolecard_embed, error_embed
from rolecard_mappings import ALIGNMENT_MAPPING, WINCON_MAPPING, WINCON_3P_MAPPING, ALIGNMENT_ROLECARD_MAPPING, \
    MIXED_ROLECARD_MAPPING, COLOR_MAPPING, MISC_MAPPING


@dataclass
class Rolecard:
    win_con: str
    alignment: str
    abilities: List[str]

    def to_string(self):
        abilities = '\n'.join([f"- {abi}" for abi in self.abilities])
        return f"""
        Welcome! You are aligned with the **{self.alignment}**. {self.win_con}
        
        The following abilities are at your disposal:
        {abilities}
        
        """.replace('the **neither the town nor mafia**', '**neither the town nor mafia**')


DRAGON_ID_PAT = re.compile(r'flightrising.com/dragon/(\d{1,9})')


def get_dragon_rolecard(link) -> Embed:
    """
    generates a rolecard based on 8 digits of the SHA 1 hash of dragon id.
    first digit: alignment
    second digit: wincon (if alignment = 3p)
    third digit: alignment-specific ability
    eighth digit: is amnesiac (if alignment = 3p)?
    """
    if not link:
        return error_embed('Please include a link to the dragon!\n\nExample:\n`/rolecard https://www1.flightrising.com/dragon/[dragonid]`')
    dragon_id = DRAGON_ID_PAT.findall(link)
    if len(dragon_id) != 1:
        return error_embed('The link is invalid. Please include a link to the dragon!')
    dragon_id = dragon_id[0]
    id_hash = hashlib.sha1(dragon_id.encode('utf-8')).hexdigest()[:8]

    alignment = ALIGNMENT_MAPPING[id_hash[0]]
    rolecard = Rolecard(
        alignment=alignment,
        win_con=WINCON_MAPPING[alignment],
        abilities=[]
    )
    if alignment == 'neither the town nor mafia':
        rolecard.win_con = WINCON_3P_MAPPING[id_hash[1]]

    rolecard.abilities += ALIGNMENT_ROLECARD_MAPPING[alignment].get(id_hash[2], [])

    rolecard.abilities += MIXED_ROLECARD_MAPPING.get(id_hash[3], [])

    if alignment != 'Mafia':
        rolecard.abilities += MISC_MAPPING.get(id_hash[4], [])

    if alignment == 'neither the town nor mafia':
        if id_hash[7] in {'1', '2'}:
            rolecard.abilities = ['**[ACTIVE]** Choose a dead player, inheriting their abililites and win condition.']
            rolecard.wincon = 'You win if you achieve the win condition of the player you inherit it from.'

    if len(rolecard.abilities) == 0:
        rolecard.abilities.append('You have no special abilities. Your power is in your voice and your vote.')

    rolecard.abilities = sorted(list(set(rolecard.abilities)))  # sort & remove duplicates
    if rolecard.alignment == 'Mafia':
        rolecard.abilities.append('**[FACTIONAL]** Kill a player of your choice.')

    return rolecard_embed(
        rolecard=f'{rolecard.to_string()}\n\n*This rolecard was generated for dragon [{dragon_id}]({link}).*',
        color=COLOR_MAPPING[alignment])


if __name__ == '__main__':
    get_dragon_rolecard('https://www1.flightrising.com/dragon/84925932')
