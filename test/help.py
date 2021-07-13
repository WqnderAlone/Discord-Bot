import discord
from helpfolder import stockhelp, covidhelp, mathhelp

prefix = "."

#class descriptions
adminDescription = 'Admin features (bot requires permissions iirc)'
annoyingDescription = 'Does all sorts of annoying stuff'
miscDescription = 'Features mainly implemented for irls'

def help(c, c1, c2):
	mathDescription = 'Can solve math equations ¯\\_(ツ)_/¯'
	adminDescription = 'Admin features (bot requires permissions iirc)'
	annoyingDescription = 'Does all sorts of annoying stuff'
	miscDescription = 'Features mainly implemented for irls'
	if c == None:
		embed = """
		`Help Page
		This page provides the description and usage of all commands
		
		Stock Market            For more information, do .help stock
		Math                    For more information, do .help math
		Covid				For more information, do .help covid`"""
	else:
		if "stock" in c:
			embed = stockhelp.stockhelp(c = c, primaryCommand = c1)
		elif "covid" in c:
			embed = covidhelp.covidhelp(c = c, primaryCommand = c1)
		elif "math" in c:
			embed = mathhelp.mathhelp(command = c, command1 = c1)

	return embed
