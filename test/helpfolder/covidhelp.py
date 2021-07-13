def covidhelp(c, primaryCommand):
	
	prefix = "."
	
	covidDescription = "Steals information using COVID19Py to get the latest information on coronavirus. "
	
	if primaryCommand == None:
		embed = f"""
`Covid Help Page
{covidDescription}

Usage:
{prefix}covid <command> <optional location>

Commands:
confirmed, recovered, deaths

Optional Parameter: Location
If you want to find the coronavirus statistics for a specified country, use the country code after the command. (i.e. {prefix}covid confirmed US)

For more information:
{prefix}help covid <command>`"""

	else:
		if "confirm" in primaryCommand:
			embed = f"""
`Covid Confirmed Cases Help Page
Finds the amount of confirmed cases worldwide or in a specified country

Usage:
{prefix}covid confirmed <*location>`"""

		elif "recover" in primaryCommand:
			embed = f"""
`Covid Recovered Cases Help Page
Finds the amount of recovered cases worldwide or in a specified country

Usage:
{prefix}covid recovered <*location>`"""

		elif "death" in primaryCommand:
			embed = f"""
`Covid Deaths Help Page
Finds the number of deaths worldwide or in a specified country

Usage:
{prefix}covid deaths <*location>`"""

























	return embed
