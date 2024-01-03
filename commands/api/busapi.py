import hikari
import lightbulb
import json

plugin = lightbulb.Plugin("BusAPI")

@plugin.command
@lightbulb.option(name="regplate", description="The registration plate of the bus.")
@lightbulb.command(name="businfo", description="Get the bus information of a company.")
@lightbulb.implements(lightbulb.SlashCommand)
async def businfo(ctx: lightbulb.SlashContext):
    with open("./commands/api/The_API.json") as file:
        try:
            upp = ctx.options.regplate.upper()
            nospace = upp.replace(" ", "")
            read = file.read()
            jread = json.loads(read)

            number = jread["results"][0][nospace]["number"]
            regplate = jread["results"][0][nospace]["reg_plate"]
            chassis = jread["results"][0][nospace]["chassis"]
            bodywork = jread["results"][0][nospace]["bodywork"]
            engine = jread["results"][0][nospace]["engine"]
            livery = jread["results"][0][nospace]["livery"]
            branding = jread["results"][0][nospace]["branding"]
            depot = jread["results"][0][nospace]["depot"]

            embed = hikari.Embed(
                title=f"Results for: ``{nospace}``",
                description=f"Number: **{number}**\nRegistration Plate: **{regplate}**\nChassis: **{chassis}**\nBodywork: **{bodywork}**\nEngi \
                ne: **{engine}**\nLivery: **{livery}**\nBranding: **{branding}**\nDepot: **{depot}**",
                colour="#3693f6"
                )
            embed.set_author(name=str(ctx.author), icon=str(ctx.author.avatar_url))
            await ctx.respond(embed=embed)
            file.close()
        except KeyError:
            errorembed = hikari.Embed(
                title="Not Found",
                description="Unfortunately, I could not find that registration plate in the data.",
                colour="#3693f6"
            )
            errorembed.set_author(name=str(ctx.author), icon=str(ctx.author.avatar_url))
            await ctx.respond(embed=errorembed)

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)
