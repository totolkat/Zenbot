import hikari
import lightbulb
from dotenv import load_dotenv
import os

load_dotenv()

intents = hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT
zenbot = lightbulb.BotApp(token=os.getenv("DISCORD_TOKEN"), intents=intents)

zenbot.load_extensions_from("./commands/general")
zenbot.load_extensions_from("./commands/api")

@zenbot.listen(hikari.StartedEvent)
async def start(event: hikari.StartedEvent):
    print(f"Zenbot has started")

zenbot.run()
