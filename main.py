import os

from flask import Flask
from flask_discord_interactions import DiscordInteractions, Option, Embed, Message

from get_dragon_rolecard import get_dragon_rolecard

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]


@discord.command()
def ping(ctx):
    "Respond with a friendly 'pong'!"
    return "Pong!"


@discord.command(options=[Option(name='link', type=3, required=False)])
def rolecard(ctx, link=None):
    "Receive a rolecard for your dragon."
    return Message(embed=get_dragon_rolecard(link))


discord.set_route("/interactions")

discord.update_commands()

if __name__ == '__main__':
    app.run(port=5000)
