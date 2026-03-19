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