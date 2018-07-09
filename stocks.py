# A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

stockDict = {"WMT": "Walmart", "AAPL": "Apple Inc", "EA": "Electronic Arts Inc"}

print(stockDict)

# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

#Step 1): Create a list of tuples.  Each tuple is a stock purchase
stockPurch = [( 'AAPL', 1000, '10-sep-2018', 100 ), ( 'EA', 1000, '1-apr-2018', 50 ), ( 'WMT', 1000, '1-jul-2018', 25 ),( 'AAPL', 2000, '20-sep-2018', 90 ), ( 'EA', 2000, '20-apr-2018', 45 ), ( 'WMT', 2000, '10-jul-2018', 20 )]

#Step 2): Loop through list of tuples and find the name of the associated stock ticker 
for purchase in stockPurch:
    # print ('Stock Purchase =', purchase)
    print ('Company Name', stockDict[purchase[0]])
    # print (price)
    price = purchase[1] * purchase[3]
    print ('Stock Purchase:', stockDict[purchase[0]] + ', ' + str(price) )

#

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.