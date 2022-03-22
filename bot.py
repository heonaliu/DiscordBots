import lightbulb
import hikari

botToken = 'OTU1ODg4OTIzOTg3NTU4NDMw.YjoO7w.LpVuRCsRt0pnFhSsS7_t_cS991U'
bot = lightbulb.BotApp.GatewayBot(
     token = botToken, 
     default_enabled_guilds = (954147091008094278))

@bot.listen(hikari.GuildMessageCreateEvent)
async def printMessage(event):
     print(event.content)
     
@bot.listen(hikari.StartedEvent)
async def botStarts(event):
     print('Bot Startup!')

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx): 
     await ctx.respond('pongie!')

@bot.command
@lightbulb.command('group', 'this is gruop!')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def myGroup(ctx):
     pass

@myGroup.child
@lightbulb.command('subcmd', 'subcmd')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subCommand(ctx):
     await ctx.respond('subbie')
     
@bot.command
@lightbulb.option('numb1', '#1', type = int )
@lightbulb.option('numb2', '#2', type = int )
@lightbulb.command('add', 'add 2 numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
     await ctx.respond(ctx.option.numb1 + ctx.option.numb2)

bot.run()