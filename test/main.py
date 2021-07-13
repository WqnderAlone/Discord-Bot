import discord
from discord.ext import commands, tasks
import time
import datetime
import os
import math1 as m
import stock as s
import covid as c
import help as h
import logger as l
import jokes as j
import crypto as cr
import misc

key = os.getenv('key')
wkey = os.getenv('wkey')
client = commands.Bot(command_prefix = ".", case_insensitive = True)
client.remove_command('help') 

@client.event
async def on_ready():
	print("ready")
	await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "your every move since 2021"))

#@client.event
#async def on_message(message):
#	l.log(author = message.author.name, authorid = message.author.id, discri = message.author.discriminator, guild = message.guild, channel = message.channel, message = message.content)
#	await client.process_commands(message)

@client.command()
async def gibberish(ctx, length):
	await ctx.send(misc.gibberish(length))

@client.command()
async def crypto(ctx, this, that):
	await ctx.send(cr.compare(this, that))

@client.command()
async def joke(ctx):
	await ctx.send(j.joke())

@client.command()
async def help(ctx, command = None, command2 = None, command3 = None):
	await ctx.send(h.help(c = command, c1 = command2, c2 = command3))

@client.command()
async def covid(ctx, command, location = None):
	await ctx.send(c.c(command = command, location = location))

@client.command()
async def stock(ctx, company, command, param = None):
	await ctx.send(f'`{s.find(company = company, command = command, time = param)}`')

@client.command()
async def math(ctx, typeEquation, eq):
	await ctx.send(m.solve(equationType = typeEquation, equation = eq))

@client.command()
async def spam(ctx, mssg):
	for i in range(0, 10):
		await ctx.send(f'{ctx.author} wrote: {mssg}')
		time.sleep(1)

@client.command()
async def test(ctx):
	await ctx.send("Operational")

@client.event
async def on_command_error(ctx, error):
	await ctx.send(f'Error: {error}')

@client.command()
async def ping(message):
	start = time.time()
	await message.channel.send("_ _")
	end = time.time()
	await message.channel.send(f'Pong! Latency: {round((end - start) * 1000)}ms')

client.run("NzUwMTY5OTU0NzM2Nzk5NzU0.X02oNg.fe98-kP6_0RMEMV2IJAw8rAA8Rk")
