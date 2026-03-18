# we will learn about conditional filtering in this python file. We will learn how to filter data in a dataframe based on certain conditions. This is a very common operation in data analysis and it is used to extract specific rows from a dataframe that meet certain criteria. We will also learn how to use multiple conditions for filtering data in a dataframe.
import pandas as pd
df_orders = pd.read_csv('files/orders.csv') 
print(df_orders.head(5))