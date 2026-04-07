# Per category basis data analyze 
# Average per group or category (categorical columns => can be string or number either of these). 

import pandas as pd
df_orders = pd.read_csv(r'files/orders.csv')
print(df_orders)

# group by itself is a lazy operation as it waits for an aggregate function.
print(df_orders.groupby('Country')) # If we only run this it means pandas has not actually done anything till now.  it is still waiting for perfomraing calculations on aggregation column. 

print(df_orders.groupby('Country').value_counts())
print('/n')
print(df_orders.groupby(['Country','Product']).value_counts()) #Returns a multi level Index. 

df_orders.groupby(['Country','Product']).value_counts()

#Contunuing the exercise below. 
# Further examples below. 