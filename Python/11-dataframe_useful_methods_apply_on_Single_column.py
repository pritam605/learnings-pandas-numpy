# Here we will talk about the use of specialized way of method calls for Pandas. 
# Apply method : Helps us apply any custom function as per our choice. We could use it on one column or many columns.

# Let's define our function:
def convertstr_last_4digits(a):
    return str(a)[-4:]

import pandas as pd
df_orders = pd.read_csv('files/orders.csv') 
print(df_orders.head(5))

print(df_orders['CustomerName'].apply(convertstr_last_4digits)) #Pandas does the function call here. we do not need to call it explicitly. 

#Since the output was series above we can create a new column based on the series. 
df_orders['new_col'] = df_orders['CustomerName'].apply(convertstr_last_4digits)
print(df_orders.head(5))

# Let's do more complex operations.
print(df_orders['Price'].mean())

def yelp(price):
    if price < 50:
        return '$'
    elif price > 50 and price < 150:
        return '$$'
    else:
        return '$$$'

df_orders['yelp'] = df_orders['Price'].apply(yelp)
print(df_orders.head(5))

# **Note: Apply method expects a single return value. We should not be returning an entire series. 

# What if we were to work with 2 columns? Till now we were only using one column in our formula.
# We now make use of Lambda functions. 
