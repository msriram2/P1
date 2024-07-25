

"""
GOAL: 

Buyer Preferences: Given a list of buyers, and the items in the dictionaries are sorted by preference. 
So for example, Buyer 1's top preference is StockA, Buyer 2's preference is StockB, and Buyer 3's 
top preference is StockA. 

Stock Preferences: Works the same way as Buyers Preferences. For example, StockA's top preference is Buyer1, 
StockB's top preference is Buyer2, and StockC's top preference is Buyer1. 

Let's say Buyer1's top preference is StockA. What is StockA's top preference then? StockA's top preference is also 
Buyer1, therefore these two preferences end up getting paired in the dictionary. 

Buyer2's Top preference is StockB. Just like stockA, Buyer2 gets matched with StockB because they are each other's top 
preferences. 

This is where it gets complicated. Buyer3's top preference is StockA, However, StockA is already matched with Buyer1, 
therefore, we look at Buyer3's second option, StockB. Unfortunately, StockB is already matched with BuyerB. The only
option left is Stock3. However, Stock3 is Buyer3's last option, and StockC's last option is Buyer3. Since both are each
other's last option, what happens now? 

Here's the Solution: 

What is BuyerA's second top preference? StockB. Unfortunately, StockB is already claimed by BuyerB, leaving StockC as 
BuyerA's last option. So let's not look at BuyerA here. 

What about StockA? StockA's second option is Buyer2, however, Buyer2 is occupied by StockB. 

Ok, what is BuyerB's second option? It's StockA, which is occupied by BuyerA. 

Ok what is StockB's second option? StockB's second option is BuyerA. Again, not free. 

It seems like Buyer3 and Stock3 will always remain final options, therefore, they will be paired together despite being 
each other's last options. That's final. 
"""

buyers_preferences = {'Buyer1': ['StockA', 'StockB', 'StockC'],
'Buyer2': ['StockB', 'StockA', 'StockC'],
'Buyer3': ['StockA', 'StockB', 'StockC']
}

stocks_preferences = {'StockA': ['Buyer1', 'Buyer2', 'Buyer3'],
'StockB': ['Buyer2', 'Buyer1', 'Buyer3'],
'StockC': ['Buyer1', 'Buyer2', 'Buyer3']
}

def stable_stock_matching(buyers_preferences, stocks_preferences):
    final_dict = {}
    for buy_key, buy_value in buyers_preferences:
        buy_index = 0
        final_buy = buy_value[-1]
        for stock_key, stock_value in stocks_preferences:
            stock_index = 0
            final_stock = stock_value[-1]
            #First: Check and see if any of the preferences are in each other's lists.
            while buy_index != final_buy and stock_index != final_stock:
                if buy_key == stock_value[stock_index] and stock_key == buy_value[buy_index]:
                    #Then check the order of preference
                    if stock_index == buy_index:
                        final_dict[buy_key] = stock_key
                        buy_index += 1
                        stock_index += 1

    return final_dict 

















