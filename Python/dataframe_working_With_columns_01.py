import pandas as pd
df_orders = pd.read_csv('files/orders.csv')
print(df_orders.head(5))

# We will look at Information based on columns 
print(df_orders['Country'].head(5)) #This will print the 'Country' column of the DataFrame which is a Series object. The index of the Series will be the same as the index of the DataFrame and the values of the Series will be the values of the 'Country' column in the DataFrame. This is an example of how to access a specific column in a DataFrame using the column name as a key.

print(df_orders.Country.head(5)) #This will also print the 'Country' column of the DataFrame which is a Series object. The index of the Series will be the same as the index of the DataFrame and the values of the Series will be the values of the 'Country' column in the DataFrame. This is another way of accessing a specific column in a DataFrame using the column name as an attribute. However, this method only works if the column name does not have any spaces or special characters and does not conflict with any existing attributes of the DataFrame. Therefore, it is generally recommended to use the first method of accessing columns using the column name as a key to avoid any potential issues with column names that may not be valid Python identifiers.

# Each of the column in the pandas series share the same Index.

cols = ['OrderID', 'CustomerName', 'Country']
print(df_orders[cols].head(5))

#Same thig as above can be done in one single step as below:
print(df_orders[['OrderID', 'CustomerName', 'Country']].head(5)) #Passing a list of column names hence double bracket.

#creating a new column
# it is similar to how we do in numpy array
df_orders['new_col'] = df_orders['Price'] * 2 #This will create a new column called 'new_col' in the DataFrame and assign it the values of the 'OrderAmount' column multiplied by 2. This is an example of how to create a new column in a DataFrame by performing an operation on an existing column. The new column will have the same index as the original DataFrame and the values will be the result of the operation performed on the existing column.
print(df_orders.head(5))

print("\n")

df_orders['new_col1'] = df_orders['Price']/df_orders['Quantity']
print(df_orders.head(5))

# If we reference the column that already existss in the df then padnas will overwrite the existing column with the new values. For example, if we do below:
df_orders['new_col1'] = df_orders['Price']*2 #This will overwrite the existing 'new_col1' column in the DataFrame with the new values which are the 'Price' column multiplied by 2. This is an example of how referencing an existing column in a DataFrame when creating a new column will overwrite the existing column with the new values. Therefore, it is important to be careful when creating new columns in a DataFrame to avoid accidentally overwriting existing columns that may contain important data.
print(df_orders.head(5))

# Since pandas is built on top of numpy we can directly use numpy universal functions on pandas almost as if they are just a wrapper around numpy. So, we can take the above operation and put it all inside a numpy function as below:
import numpy as np  
df_orders['new_col2'] = np.round(df_orders['Price'], 2) #This will create a new column called 'new_col2' in the DataFrame and assign it the values of the natural logarithm of the 'Price' column. This is an example of how to use a numpy universal function on a pandas Series to create a new column in a DataFrame. The new column will have the same index as the original DataFrame and the values will be the result of applying the numpy function to the existing column.
print(df_orders.head(5))

# Removing columns
# df_orders.drop() # general command to drop columns. we can either pass one col or a list of col
# axis = 0 means drop row and axis = 1 as if they were a column

# df_orders.drop('new_col2') # Writing this will result me an error becase by default axis is 0 so it is trying to drop a row with the label 'new_col2' which does not exist in the DataFrame. To drop a column, we need to specify axis=1 in the drop() method. For example, df_orders.drop('new_col2', axis=1) will drop the 'new_col2' column from the DataFrame. This is an example of how to use the drop() method to remove a column from a DataFrame by specifying the column name and the axis parameter.

df_orders.drop('new_col2', axis=1, inplace=True) #This will drop the 'new_col2' column from the DataFrame and modify the original DataFrame in place. The inplace parameter is used to specify whether we want to modify the original DataFrame or return a new DataFrame with the column dropped. If inplace=True, it will modify the original DataFrame and return None. If inplace=False (which is the default), it will return a new DataFrame with the column dropped and leave the original DataFrame unchanged. This is an example of how to use the drop() method to remove a column from a DataFrame and modify the original DataFrame in place by setting inplace=True.

# inplace is going to be depricated in future so we recommend to do it like df_orders = df_orders.drop('new_col2', axis=1) 

# why axis = 0 is rows because it is dervied from numpy array shape. when we do df.shape then first output that comes out is rows hence we say axis = 0 is rows and axis = 1 is columns.

