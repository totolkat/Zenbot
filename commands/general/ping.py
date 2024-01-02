import hikari
import lightbulb

plugin = lightbulb.Plugin("Ping")

@plugin.command
@lightbulb.command(
    name="ping",
    description="Checks the bot's response time."
)
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    latency = plugin.app.heartbeat_latency * 1000
    embed = hikari.Embed(
        title=":ping_pong: Pong!",
        description=f"Latency: ``{latency:,.0f}``ms",
        color="#3693f6"
    )
    await ctx.respond(embed=embed)

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)
