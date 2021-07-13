
def stockhelp(c, primaryCommand):
	prefix = "."
	
	stockDescription = 'Steals Information on the Stock Market via a Yahoo! Finance API :D'
	
	if primaryCommand == None:
		embed = f"""
`Stock Help Page
{stockDescription}		

Usage:
{prefix}stock <command> <optional parameters>

Commands:
history,actions, dividends, financials, quarterlyfinancials

For more information:
{prefix}help stock <command>`"""
	else:
		if 'history' in primaryCommand:
			embed = f"""
`Stock History Help Page
Takes the history of a given stock with an optional time parameter

Usage:
{prefix}stock <company> history <timeframe>

Timeframe Examples:
"5d" for 5 days
"max" for all time`"""
	
		elif 'action' in primaryCommand:
			embed = f"""
`Stock Actions Help Page
Returns the company's dividends and splits

Usage:
{prefix}stock <company> actions`"""

		elif 'divid' in primaryCommand:
			embed = f"""
`Stock Dividends Help Page
Returns the company's dividends

Usage:
{prefix}stock <company> dividends`"""

		elif 'finan' in primaryCommand:
			if 'quar' in primaryCommand:
				embed = f"""
`Stock Quarterly Financials Help Page
Returns the company's quartly financials

Usage:
{prefix}stock <company> quarterlyfinancials`"""
			else:
				embed = f"""
`Stock Financials Help Page
Returns the company's financials

Usage:
{prefix}stock <company> financials`"""

		elif ('major' in primaryCommand) and ('hold' in primaryCommand):
			embed = f"""
`Stock Major Holders Help Page
Returns a company's major holders

Usage:
{prefix}stock <company> majorholders`"""

		elif ('instit' in primaryCommand) and ('hold' in primaryCommand):
			embed = f"""
`Stock Institutional Holders Help Page
Returns a company's institutional holders

Usage:
{prefix}stock <company> institutional holders`"""









































	return embed
