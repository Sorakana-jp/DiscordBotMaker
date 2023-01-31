import discord
from discord.ext import commands
from discord_buttons_plugin import *
from pyfiglet import Figlet

bot = commands.Bot(command_prefix = "YourCommand!")
buttons = ButtonsClient(bot)

token = "BotToken"

@bot.event
async def on_ready():
	f = Figlet(font='slant')
	g = f.renderText('BotName')
	print(g)
	h = f.renderText('   By YourName')
	print(h)
	print('ログインしました')

@buttons.click
async def A1(ctx):
        await ctx.reply("YourMessage1")

@buttons.click
async def A2(ctx):
        await ctx.reply("YourMessage2")

@buttons.click
async def A3(ctx):
        await ctx.reply("YourMessage3")

@bot.command()
async def Command1(ctx):
        await buttons.send(
                
		content = "buttonMes", 
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					label="l1", 
					style=ButtonType().Danger, 
					custom_id="A1"
				)
			]),ActionRow([
				Button(
					label="l2", 
					style=ButtonType().Success, 
					custom_id="A2"
				)
			]),ActionRow([
				Button(
					label="l3",
					style=ButtonType().Primary,
					custom_id="A3"
				)
			])
		]
	)

bot.run(token)
