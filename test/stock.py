import yfinance as yf

def find(company, command, time = None):
	
	command.lower()
	
	company = yf.Ticker(company)
	
	if command == "history":
		stockhistory = company.history(period = time)
		return stockhistory
	
	elif command == "action" or command == "actions":
		stockaction = company.actions
		return stockaction
		
	if "divid" in command:
		stockdiv = company.dividends
		return stockdiv
	
	elif "split" in command:
		stocksplit = company.splits
		return stocksplit
	
	elif "financial" in command:
		if "quar" in command:
			stockfin = company.quarterly_financials
		else:
			stockfin = company.financials
		return stockfin
		
	elif ("major" in command) and ("hold" in command):
		stockhold = company.major_holders
		return stockhold
		
	elif ("institu" in command) and ("hold" in command):
		stockhold = company.institutional_holders
		return stockhold
