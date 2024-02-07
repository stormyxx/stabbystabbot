ALIGNMENT_MAPPING = {
    '0': 'neither the town nor mafia',
    '1': 'neither the town nor mafia',
    '2': 'neither the town nor mafia',
    '3': 'Mafia',
    '4': 'Mafia',
    '5': 'Mafia',
    '6': 'Mafia',
    '7': 'Town',
    '8': 'Town',
    '9': 'Town',
    'a': 'Town',
    'b': 'Town',
    'c': 'Town',
    'd': 'Town',
    'e': 'Town',
    'f': 'Town'
}

COLOR_MAPPING = {
    'Town': 1752220,
    'Mafia': 15548997,
    'neither the town nor mafia': 15105570
}
WINCON_MAPPING = {
    'Town': 'You win if all threats to the town have been eliminated, and at least one town member is alive.',
    'Mafia': 'You win if your faction makes up half of the remaining alive players, or if nothing can prevent this.',
    'neither the town nor mafia': ''
}

WINCON_3P_MAPPING = {
    '0': 'You win if you are eliminated.',
    '1': 'You win if you are eliminated.',
    '2': 'You win if you are eliminated.',
    '3': 'You win if you are the last remaining player alive, or when nothing can prevent this.',
    '4': 'You win if you are the last remaining player alive, or when nothing can prevent this.',
    '5': 'You win if you are the last remaining player alive, or when nothing can prevent this.',
    '6': 'You win if you are the last remaining player alive, or when nothing can prevent this.',
    '7': 'You win if you are the last remaining player alive, or when nothing can prevent this.',
    '8': 'You win if you are the last remaining player alive, or when nothing can prevent this.',
    '9': 'You win if you and your lover are both alive at the end of the game.',
    'a': 'You win if you and your lover are both alive at the end of the game.',
    'b': 'You win if you are alive at the end of the game.',
    'c': 'You win if you are alive at the end of the game.',
    'd': 'You win if you are alive at the end of the game.',
    'e': 'You win when the mod is eliminated >:)'
}

MAFIA_ROLECARD_MAPPING = {
    '0': ['**[PASSIVE]** You show up as town when investigated.'],
    '1': ['**[PASSIVE]** You show up as town when investigated.'],
    '2': ['**[PASSIVE]** You show up as town when investigated.'],
    '3': [
        '**[ACTIVE][1-SHOT]** Upgrade your factional kill tonight to pierce through any protection your target may have.'],
    '4': [
        '**[ACTIVE][1-SHOT]** Upgrade your factional kill tonight to pierce through any protection your target may have.'],
    '5': ['**[ACTIVE]** Make your target appear as Mafia if investigated for the night.'],
    '6': ['**[ACTIVE]** Make your target appear as Mafia if investigated for the night.'],
    '7': ['**[ACTIVE][1-SHOT]** Convert a player of your choice, making them mafia-aligned.'],
    '8': [
        '**[ACTIVE]** Roleblock a player of your choice, preventing them from using any active abilities for the night.'],
    '9': ['**[ACTIVE]** Redirect a player of your choice, making them target another player of your choice instead.'],
    'a': [
        '**[ACTIVE][1-SHOT]** Pick a player of your choice. When they die, their alignment and rolecard will not be revealed.'],
    'e': ['**[ACTIVE]** Douse a player with gasoline.',
          '**[ACTIVE]** Set all players that have been doused with gasoline on fire, killing them.']

}

THREE_P_ROLECARD_MAPPING = {
    '0': ['**[ACTIVE]** Douse a player with gasoline.',
          '**[ACTIVE]** Set all players that have been doused with gasoline on fire, killing them.'],
    '1': ['**[ACTIVE]** Douse a player with gasoline.',
          '**[ACTIVE]** Set all players that have been doused with gasoline on fire, killing them.'],
    '2': ['**[ACTIVE]** Douse a player with gasoline.',
          '**[ACTIVE]** Set all players that have been doused with gasoline on fire, killing them.'],
    '3': ['**[ACTIVE]** Douse a player with gasoline.',
          '**[ACTIVE]** Set all players that have been doused with gasoline on fire, killing them.'],
    '4': ['**[ACTIVE]** Douse a player with gasoline.',
          '**[ACTIVE]** Set all players that have been doused with gasoline on fire, killing them.'],
    '5': ['**[ACTIVE][NON-CONSECUTIVE]** Kill a player of your choice.'],
    '6': ['**[ACTIVE][NON-CONSECUTIVE]** Kill a player of your choice.'],
    '7': ['**[ACTIVE][NON-CONSECUTIVE]** Kill a player of your choice.'],
    '8': ['**[ACTIVE][NON-CONSECUTIVE]** Kill a player of your choice.'],
    '9': ['**[ACTIVE][NON-CONSECUTIVE]** Kill a player of your choice.'],
    'a': ['**[ACTIVE][NON-CONSECUTIVE]** Kill a player of your choice.'],
    'b': ['**[PASSIVE]** If you die via any means, the player who has last visited you will die with you.'],
    'c': ['**[ACTIVE][2-SHOT]** Put on a bullet-proof vest. Under normal circumstances, you cannot be killed tonight.'],
    'd': ['**[ACTIVE][2-SHOT]** Put on a bullet-proof vest. Under normal circumstances, you cannot be killed tonight.'],
    'e': ['**[ACTIVE][2-SHOT]** Put on a bullet-proof vest. Under normal circumstances, you cannot be killed tonight.'],
    'f': ['**[ACTIVE]** Poison a player of your choice. They will die if not healed within 2 days.']
}

TOWN_ROLECARD_MAPPING = {
    '0': ['**[ACTIVE]** Investigate the alignment of a player of your choice.'],
    '1': ['**[ACTIVE]** Investigate the alignment of a player of your choice.'],
    '2': ['**[ACTIVE]** Watch a player of your choice. You will learn who visited them tonight.'],
    '3': ['**[ACTIVE]** Pick two players. You will learn if they are of the same alignment.'],
    '4': ['**[PASSIVE]** If you are targeted by a killing action, you will kill your attacker.'],
    '5': ['**[ACTIVE]** Kill a player of your choice.'],
    '6': [
        '**[ACTIVE]** Heal a player of your choice. They will not die if they are attacked under normal circumstances.'],
    '7': [
        '**[ACTIVE]** Heal a player of your choice. They will not die if they are attacked under normal circumstances.'],
    '8': ['**[ACTIVE][1-SHOT]** Reveal all visits that took place during the night on the next Start of the Day post.'],
    '9': ['**[ACTIVE][1-SHOT]** Reveal all visits that took place during the night on the next Start of the Day post.'],
    'a': ['**[LIGHTNING][1-SHOT]** Have the mod confirm that you are aligned with the town on the thread.'],
    'b': ['**[LIGHTNING][1-SHOT]** Have the mod confirm that you are aligned with the town on the thread.'],
    'c': [
        '**[ACTIVE]** Guard a player of your choice. If they are killed during the night, you will die in their place.'],
    'd': [
        '**[ACTIVE]** Guard a player of your choice. If they are killed during the night, you will die in their place.']
}

MIXED_ROLECARD_MAPPING = {
    '0': [
        '**[ACTIVE]** Roleblock a player of your choice, preventing them from using any active abilities for the night.'],
    '1': ['**[PASSIVE]** You will reveal all players that visit you during the night in the Start of Day post.'],
    '2': ['**[ACTIVE]** Redirect a player of your choice, making them target another player of your choice instead.'],
    '3': [
        '**[ACTIVE]** Switch any two players of your choice. Abilities targeting a switched player will target the other player instead.'],
    '4': ['**[ACTIVE][LIGHTING][1-SHOT]** Kill a player of your choice.'],
    '6': ['**[ACTIVE][2-SHOT]** Stay on alert, killing any players that visit you during the night.'],
    '7': ['**[ACTIVE][2-SHOT]** Stay on alert, killing any players that visit you during the night.'],
    '8': [
        '**[ACTIVE][2-SHOT]** Hide in your quarters for the night, making all non-killing actions performed on you fail.'],
    '9': ['**[ACTIVE]** Send a message of up to 50 words to a player of your choice.'],
    'a': ['**[ACTIVE]** Watch a player of your choice. You will learn who visited them tonight.'],
    'b': ['**[ACTIVE]** Track a player of your choice. You will learn who they visited tonight.'],
    'c': ['**[ACTIVE][1-SHOT]** Learn about all abilities possessed by a player of your choice.'],
    'd': ['**[ACTIVE]** Poison a player of your choice. They will die if not healed within 2 days.']
}

ABILITY_ENHANCER_MAPPING = {
    '0': ['**[ACTIVE][1-SHOT][DAY]** Upgrade your ability tonight to target up to three players.'],
    '1': ['**[ACTIVE][1-SHOT][DAY]** Upgrade your ability tonight to target all players that visit you tonight.'],
    '2': ['**[ACTIVE][1-SHOT]** Give a single-use copy of any of your abilities to a player of your choice.'],
}

MISC_MAPPING = {
    '0': ['**[PASSIVE]** You will always alert your target of your visit.'],
    '1': ['**[PASSIVE]** Your vote will count as two votes.'],
    '5': ['**[PASSIVE]** You will show up as Mafia when investigated.'],
    'e': ['**[PASSIVE]** You will die if you target a mafia-aligned player.']
}

ALIGNMENT_ROLECARD_MAPPING = {'Mafia': MAFIA_ROLECARD_MAPPING, 'Town': TOWN_ROLECARD_MAPPING,
                              'neither the town nor mafia': THREE_P_ROLECARD_MAPPING}
