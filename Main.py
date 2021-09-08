#!/usr/bin/env python3
from array import *
from time import time, sleep
import robin_stocks
import robin_stocks.robinhood as r
import yfinance as yf
from ListFunc import *

#userName = input("Please enter your username:\n")
#passWord = input("Please enter your password:\n")

userName = 'tanishmeh@icloud.com'
passWord = 'Hariom2002'

import robin_stocks.robinhood as r
login = r.login(userName, passWord)

holdings = ''
runLoop = True
secondsRun = 0

my_stocks = r.build_holdings() # builds the two dimensional dictionary with {APPL, {DATA:DATA}}
crypto_positions = r.get_crypto_positions()

cryptoHoldings = createCryptoList(crypto_positions)
stockHoldings = createStockList(my_stocks)

# Authentication and Initiation Area
# --------------------------------------------------------------------

while runLoop == True:
	sleep(2 - time() % 2)
	
	
	
	