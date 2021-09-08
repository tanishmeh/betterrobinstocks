#!/usr/bin/env python3
from array import *
from time import time, sleep
import robin_stocks
import robin_stocks.robinhood as r

#userName = input("Please enter your username:\n")
#passWord = input("Please enter your password:\n")

userName = 'tanishmeh@icloud.com'
passWord = 'Hariom2002'

import robin_stocks.robinhood as r
login = r.login(userName, passWord)

holdings = ''
priceList = []
holdingItems = 0
runTimes = 0

# End of Authentication and Initiation Area
# --------------------------------------------------------------------

def createSingleStockList(keyList, index, my_stocks):
	tempList = []
	tempList.append(keyList[index])
	temp = my_stocks[keyList[index]]
	tempList.append(temp['price'])
	tempList.append(temp['quantity'])
	tempList.append(temp['average_buy_price'])
	tempList.append(temp['type'])
	tempList.append(temp['name'])
	return tempList
	
# End of returning a single list containing information for a single stock
# --------------------------------------------------------------------
	
def createSingleCryptoList(cryptoList, index, crypto_positions, price1):
	tempList = []
	temp0 = crypto_positions[index]
	temp1 = temp0.get('currency')
	temp2 = temp1.get('code')
	tempList.append(temp2)
	tempList.append(price1) # this is supposed to be the price
	tempList.append(temp0.get('quantity'))
	tempList.append(-1) # didn't add avg. price functionality yet
	tempList.append(temp1.get('type'))
	tempList.append(temp1.get('name'))
	return tempList

# End of returning a single list containing information for a single stock
# --------------------------------------------------------------------

def createKeyList(my_stocks):
	keyList = []
	for key in my_stocks.keys():
		keyList.append(key)
	return keyList

# End of creating a list of symbols from my_stocks
# --------------------------------------------------------------------

def createCryptoKeyList(crypto_positions):
	keyList = []
	for i in range(len(crypto_positions)):
		temp = crypto_positions[i].get('currency')
		keyList.append(temp.get('code'))
	return keyList

# End of creating a list of symbols from crypto_positions
# --------------------------------------------------------------------

def createPriceList(keyList, index):
	tempList = []
	tempList.append(keyList[index])
	temp = my_stocks[keyList[index]]
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
	
def addPrice(price, symbol):
	temp = priceList[getSymbolIndexFromList(priceList, symbol)]
	temp.append(price)
	priceList[getSymbolIndexFromList(priceList, symbol)] = temp
	
# End of adding a price to priceList for a certain symbol and inputting the newer price
# --------------------------------------------------------------------
	
def getCurrentPrice(symbol):
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



while True: # each iteration is about 2 seconds (plus processing and receiving data time, which is a little more)
	sleep(2 - time() % 2)
	
	my_stocks = r.build_holdings() # builds the two dimensional dictionary with {APPL, {DATA:DATA}}
	crypto_positions = r.get_crypto_positions()
	
	Matrix = []
	
	keyList = createKeyList(my_stocks)
	cryptoList = createCryptoKeyList(crypto_positions)

	lenKeyList = len(keyList)
	iterMatrix = 0
	
	if runTimes == 0:
		for i in range(len(keyList)):
			priceList.append(createPriceList(keyList, i))
	
	for i in range(lenKeyList):
		Matrix.append(createSingleStockList(keyList, i, my_stocks))
		addPrice(Matrix[i][1], getSymbolFromList(Matrix, i))
		
	
#	if keyList.sort() != priceList.sort():
#		for i in range(lenKeyList):
#			if keyList[i] != getSymbolFromList(priceList, i):
#				priceList.insert(i, createPriceList(keyList, i))
	

	print(Matrix)
	print(priceList)
	print (cryptoList)
	print(crypto_positions)
	
	print(createSingleCryptoList(cryptoList, 2, crypto_positions, 100))
	
	
	runTimes += 1
	