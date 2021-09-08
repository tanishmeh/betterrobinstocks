#!/usr/bin/env python3

def createCryptoList(crypto_positions):
	keyList = []
	for i in range(len(crypto_positions)):
		if float(crypto_positions[i].get('quantity')) > 0.0:
			temp = crypto_positions[i].get('currency')
			tempList = []
			tempList.append(temp.get('code'))
			tempList.append(temp.get('name'))
			tempList.append(crypto_positions[i].get('quantity'))
			keyList.append(tempList)
	return keyList

# End of creating a list of symbols from crypto_positions [[SYMBOL1, CODE, NAME], [SYMBOL2, CODE2, NAME2], ...]
# --------------------------------------------------------------------

def createStockList(my_stocks):
	keyList = []
	for key in my_stocks.keys():
		tempList = []
		tempList.append(key)
		tempList.append((my_stocks[key])['name'])
		tempList.append((my_stocks[key])['quantity'])
		keyList.append(tempList)
		keyList.sort()
	return keyList

# End of creating a list of symbols from my_stocks [[SYMBOL1, CODE, NAME], [SYMBOL2, CODE2, NAME2], ...]
# --------------------------------------------------------------------