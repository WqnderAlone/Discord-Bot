def mathhelp(command, command1):
	prefix = "."
	mathDescription = 'Can solve math equations ¯\\_(ツ)_/¯'
	if command == None:
		embed = f"""
`Math Help Page
{mathDescription}

Usage:
{prefix}math <command> <equation>

Commands:
algebra, calc

For more information:
{prefix}help math <command>`"""
	else:
		if "alg" in command1:
			embed = f"""
`Math Algebra Help Page
Solves basic algebra

Usage:
{prefix}math alg <equation>

Note:
Users cannot use short hand notation. For example, 2x will result in an error. Use 2*x`"""
		elif "calc" in command1:
			embed = f"""
`Math Calculations Help Page:
Solves basic problems including addition, subtraction, multiplication, division, and exponents

Usage:
{prefix}math calc <equation>`"""






































	return embed
