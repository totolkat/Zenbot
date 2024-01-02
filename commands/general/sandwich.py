import hikari
import lightbulb

plugin = lightbulb.Plugin("Ping")

@plugin.command
@lightbulb.command(
    name="sandwhich",
    description="Sandwich? Bread!"
)
@lightbulb.implements(lightbulb.SlashCommand)
async def sandwich(ctx: lightbulb.SlashContext):
    await ctx.respond("Respond with either sandwich or bread!")
    try:     
        message = await plugin.bot.wait_for(
            hikari.GuildMessageCreateEvent, 
            predicate=lambda e: (e.author_id == ctx.author.id),
            timeout=30)
        
        match message.message.content.lower():
            case "sandwich":
                await ctx.respond("Bread!")
            case "bread":
                await ctx.respond("Sandwich!")
            case _:
                await ctx.respond("What? You choose to say neither?")
        
    except TimeoutError:
        await ctx.respond("Timeout reached! You didn't respond in time.")

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)