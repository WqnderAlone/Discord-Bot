import cryptocompare

def compare(this, that):
	price = cryptocompare.get_price(this, that)
	
	return price
