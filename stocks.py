# A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

stockDict = {"WMT": "Walmart", "AAPL": "Apple Inc", "EA": "Electronic Arts Inc"}

print(stockDict)

# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

#Step 1): Create a list of tuples.  Each tuple is a stock purchase
stockPurch = [( 'AAPL', 1000, '10-sep-2018', 100 ), ( 'EA', 1000, '1-apr-2018', 50 ), ( 'WMT', 1000, '1-jul-2018', 25 ),( 'AAPL', 2000, '20-sep-2018', 90 ), ( 'EA', 2000, '20-apr-2018', 45 ), ( 'WMT', 2000, '10-jul-2018', 20 )]

#Step 2): Loop through list of tuples and find the name of the associated stock ticker
# Can also do this with a try/catch and an append.... 
for purchase in stockPurch:
    # print ('Stock Purchase =', purchase)
    print ('Company Name', stockDict[purchase[0]])
    # print (price)
    price = purchase[1] * purchase[3]
    print ('Stock Purchase:', stockDict[purchase[0]] + ', ' + str(price) )


# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

#Step 1: Create a dictionary
purchase_summary = {}

#Step 2:  Loop thru the list of tuples
for purchase in stockPurch:

    #if ticker exists in purchase_summary dictionary
    if purchase[0] in purchase_summary:
        ticker = purchase[0]
        indiv_purch = [(purchase[1], purchase[2], purchase[3])]
        #append the purchase to the ticker key
        # purchase_summary[purchase[0]] += [(purchase[1], purchase[2], purchase[3])]

        #this also works
        purchase_summary[ticker].append(indiv_purch)

    #if ticker key doesn't exist,
    else:
        #add the new ticker and the associated purchases
        purchase_summary[purchase[0]] = [(purchase[1], purchase[2], purchase[3])]

print(purchase_summary)

#Steve's solution:
# portfolio = dict()
# for purchase in purchases:
#     ticker = purchase[0]

#     full_company_name = stockDict[ticker]
#     number_of_shares = purchase[1]
#     purchase_price = purchase[3]
#     full_purchase_price = number_of_shares * purchase_price

#     minimal_purchase = (purchase[1], purchase[2], purchase[3])

#     try:
#         portfolio[ticker].append(purchase) # Append the purchase to the ticker list
#     except KeyError:
#         portfolio[ticker] = list() # If the key doesn't exist yet, create it
#         portfolio[ticker].append(purchase)


#     print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

# print(portfolio)







# for ticker,purchases in portfolio.items():
#     print("------ {} ------".format(ticker))
#     total_portfolio_stock_value = 0
#     for purchase in purchases:
#         total_portfolio_stock_value += purchase[1] * purchase[3]
#         print("    {}".format(purchase))
#     print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))