# Here let's try to use apply function via multiple methods. 
# We will make use of Lambda functions. 

import pandas as pd
df_orders = pd.read_csv('files/orders.csv') 
print(df_orders.head(5))

# Let's write a function the normal way.
def fun(num):
    return num * 2

# If we try to convert this to a lambda function i.e., anonymous function that means we do not need the name of the function and the def keyword rather we replace it with lambda keyword directly. 

# lambda num:

# for the second line, we remove the return keyword and write it all in a single line. 

lambda num: num * 2

# Complex functions cannot be converted into a lambda expression. So, we cannot make use of lambda functions all the time. 

# we can apply a single lambda function to a column. 
df_orders['New_Price'] = df_orders['Price'].apply(lambda num: num*2) #Lambda take in a Price value and multiple it by 2 . the variable for lambda can be anything. 

df_orders.head(5)
#using multiple columns for apply method

def multi_col_method(Price, Quantity):
    fnl_amt = Price * Quantity
    return fnl_amt

# print(df_orders[['Price','Quantity']].apply(multi_col_method)) -- this fails because multi column method calling is not applicable like this. 

print(df_orders[['Price','Quantity']].apply(lambda df_orders: multi_col_method(df_orders['Price'],df_orders['Quantity']), axis = 1))  #axis = 1 tells that these are columns and not index.

df_orders['new_col'] = df_orders[['Price','Quantity']].apply(lambda df_orders: multi_col_method(df_orders['Price'],df_orders['Quantity']), axis = 1)

print(df_orders.head(10))

#we can scale all this to use more columns. 
#to make this all factor we can use np.vectorize

import numpy as np
df_orders['new_col1'] = np.vectorize(multi_col_method)(df_orders['Price'],df_orders['Quantity'])

print(df_orders)
# The job of np.vectorize function is to transform functions that are not numpy aware. The regular Python function, code is not aware that we would be using the function on a numpy dataframe.

#Hence it is always good to use np.vectorize method. 