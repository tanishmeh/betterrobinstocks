#!/usr/bin/env python3

def createSingleStockList(keyList, i, my_stocks, Matrix):
	tempList = []
	tempList.append(keyList[i])
	temp = my_stocks[keyList[i]]
	tempList.append(temp['price'])
	tempList.append(temp['quantity'])
	tempList.append(temp['average_buy_price'])
	tempList.append(temp['type'])
	tempList.append(temp['name'])
	Matrix.append(tempList)
	
# End of creating a single list containing information for a single stock
# --------------------------------------------------------------------
	
def createKeyList(stocks):
	keyList = []
	for key in stocks.keys():
		keyList.append(key)
	return keyList

# End of creating a list of keys from my_stocks (stocks)
# --------------------------------------------------------------------

def createPriceList(keyList, i, my_stocks):
	tempList = []
	tempList.append(keyList[i])
	temp = my_stocks[keyList[i]]
	tempList.append(temp['price']) #This will only add the first price, as a list
	return tempList

# End of creating a single list containing symbol and a list of prices, used as an initializer for a new security
# --------------------------------------------------------------------

def getSymbolListFromList(List):
	temp = []
	for index in range(len(List)):
		temp.append(getSymbolFromPriceList(List, index))
	return temp

# End of returning a list of symbols from a list
# --------------------------------------------------------------------

def getSymbolFromList(List, index):
	if (index - 1) > len(List):
		return ''
	else:
		return List[index][0]
	
# End of returning a single symbol given an index to take from a list
# --------------------------------------------------------------------
	
def addPrice(price, symbol, priceList):
	temp = priceList[getSymbolIndexFromList(priceList, symbol)]
	temp.append(price)
	priceList[getSymbolIndexFromList(priceList, symbol)] = temp
	print(temp)
	
# End of adding a price to priceList for a certain symbol and inputting the newer price
# --------------------------------------------------------------------
	
def getCurrentPrice(symbol, Matrix):
	for index in len(Matrix):
		if Matrix[index][0] == symbol:
			return Matrix[index][1]
	return -1

# End of getting a current price of a symbol by using the Matrix list
# --------------------------------------------------------------------

def getSymbolIndexFromList(priceList, symbol):
	for i in range(len(priceList)):
		if symbol == priceList[i][0]:
			return i
	return -1

# End of getting the index for a symbol by using a list and finding the symbol (specifically used for priceList)
# --------------------------------------------------------------------