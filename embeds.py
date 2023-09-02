from flask_discord_interactions import Embed
from flask_discord_interactions.models.embed import Footer


def error_embed(message: str) -> Embed:
    return Embed(
        title="Oh no :')",
        description=message,
        color=15548997
    )


def rolecard_embed(rolecard: str, color: int) -> Embed:
    return Embed(description=rolecard, color=color)
