def create_new_dictionary(prices):
    new_dict = {}
    for key, value in prices.items():
        if value>200:
            new_dict[key]=value
    
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))

# Whole code in oneline using comprehension
def create_new_dictionary(prices):
    return {key:value for key, value in prices.items() if value>200}

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))
