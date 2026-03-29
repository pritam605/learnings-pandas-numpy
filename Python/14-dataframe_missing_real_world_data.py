#Handling missing datas. 

import pandas as pd

df_orders = pd.read_csv(r'files/orders.csv')
print(df_orders.head(5))
                        
# Missing data in pandas are represented as NaN values. 
# Null timestamps are now represented as NaT in pandas. 

# Many methods does not support NaN so we need to handle it hence we need handling techniques. 

# We can also drop of remove the missing data. but this can lead to potential loss of data or information.

# When should we drop a row vs drop a column?

#np.nan is used to display null value
# pd.NA can also be used

# pd.NAT to represent timestamps.

# np.nan is not equal to np.nan so np.nan == np.nan returns false

# Hence do not use equality, rather write it like "np.nan is np.nan" this way it returns true.
#e.g.,
import numpy as np
myvar = np.nan

print(myvar is np.nan)

# Handling missing data - 
# With pandas we can drop the entire row or an entire column that is missing based on conditions. This cna lead to missing of useful data and limits training data. 

#We can impute the missing data as well with statistical estimation. 
# We may end up dropping imporant missing data or columns. 
# Let's read a file with empty values. 
import pandas as pd
#pd.read_csv

df_orders = pd.read_csv(r'files/orders.csv')
print(df_orders.head(5))

print(
    
    df_orders.isnull() #df_orders.notnull()
      
      )

print(df_orders[df_orders['Category'].notnull()]) #Applied conditional filtering to select not null cases from df_orders. 

print(df_orders[df_orders['Category'].isnull()]) #Returns blank because all are filled. no null cases

print(df_orders[df_orders['Category'].isnull() & df_orders['Country'].isnull()])

#Handling missing data via Threshold
# thres = xx where xx means the row should have atleast that many non null values
df_orders(thres=5) # Meaning drop rows where the orders dataframe doe snot contain atleast 5 non null values. Note that this is doing row wise filtering. 

df_orders.dropna(axis=1) #axis 1 means columns so what this tells is every column that has a missing value drop them.

df_orders.dropna(axis=0) #axis 0 means rows so what this tells is every rows that has a missing value drop them.

df_orders.dropna(subset = ['last_name']) #Only considers certain column to look for missing values in those columns only. 

df_orders.dropna(thres = 4, subset = ['last_name']) # This way we can keep a combination of threshold function along with subset functions. So, any row where number of non-null vavlues are more than 4, it is going to drop it off only if last_name is null for that row. 