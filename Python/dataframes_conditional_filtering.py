# we will learn about conditional filtering in this python file. We will learn how to filter data in a dataframe based on certain conditions. This is a very common operation in data analysis and it is used to extract specific rows from a dataframe that meet certain criteria. We will also learn how to use multiple conditions for filtering data in a dataframe.
import pandas as pd
df_orders = pd.read_csv('files/orders.csv') 
print(df_orders.head(5))

# Earlier we saw row or column filtering based on a position or index. But in actual data sets the data size is huge so we may not know which row or column we want to filter based on the position or index. Therefore, we need to filter data based on certain conditions. This allows us to filterbased off a condition on the column. For example, if we want to filter the rows where the 'Price' column is greater than 50, we can do it via below:
filtered_df = df_orders[df_orders['Price'] > 50] #This will filter the rows of the DataFrame where the values in the 'Price' column are greater than 50 and return a new DataFrame with the filtered rows. The condition df_orders['Price'] > 50 creates a boolean Series where the values that satisfy the condition are True and the values that do not satisfy the condition are False. When we use this boolean Series to index the original DataFrame, it will return only the rows where the condition is True, effectively filtering the DataFrame based on the specified condition.
print(filtered_df.head(5))  

# Since we are filtering now based on condition it becomes imporatnt in general on how we are organizing our data in general specially when we move further to Machine learning. every single column becomes a feature or an attribute of a row. Row themselves are the instances of the data. Every row be a particular id with certain attributes described in column. 

# Example: What countries have Quantities Price greater than 50?
# Here we first locate what column we need to filter the data on. 
# The column that we are interested is basically a pandas series on which we will apply our conditional filter.
df_orders['Price'] > 50 #Pandas broadcase this number 50 to every single instance into the column Price and then it will return a boolean series for every instance where the values that satisfy the condition are True and the values that do not satisfy the condition are False. This is an example of how pandas applies a conditional filter to a Series by broadcasting the condition to each element in the Series and returning a boolean Series as a result.

print(df_orders[df_orders['Price'] > 50]) #Here we pass it back to the dataframe so that we get the filtered dataframe output.

#Let's look at filtering with multiple conditions. 
