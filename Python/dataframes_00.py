import pandas as pd
import numpy as np

# Here we will learn about dataframes
# Dataframes are nothing but a group of series objects that share the same index. It is a 2-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table, or a dictionary of Series objects.

# Example of a series vs dataframe
mySeries = pd.Series([10,20,30], index=['a','b','c']) #This will create a Series object with the data and index provided. The data parameter is used to specify the values of the Series and the index parameter is used to specify the labels for the index of the Series. If we do not provide an index, it will default to a numeric index starting from 0.
print(mySeries) #This will print the Series object which is a one-dimensional array with the index as 'a','b','c' and the values as 10,20,30. The index is shown on the left side and the values are shown on the right side.

# Example of a dataframe
myDataFrame = pd.DataFrame({'Column1': [10,20,30], 'Column2': [40,50,60]}, index=['a','b','c']) #This will create a DataFrame object with the data and index provided. The data parameter is used to specify the values of the DataFrame and the index parameter is used to specify the labels for the index of the DataFrame. If we do not provide an index, it will default to a numeric index starting from 0.
print(myDataFrame) #This will print the DataFrame object which is a two-dimensional array with the index as 'a','b','c' and the columns as 'Column1' and 'Column2'. The index is shown on the left side and the columns are shown on the top. The values of the DataFrame are shown in the cells where the index and columns intersect. This is an example of a DataFrame object in Pandas, which is a two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table, or a dictionary of Series objects.



# Let's create a dataframe first without column argument by just giving data and index as an argument the way we did in series exercise. Next we will add columns argument to the dataframe and see how it changes the output.

mydata = [10,20,40,70]
myIndex = ['A','B','C','D']

#print(np.array(mydata))
mydf = pd.DataFrame(data = mydata, index = myIndex)
print(mydf)

columns = ['colA']
mydf = pd.DataFrame(data = mydata, index = myIndex, columns = columns)
print(mydf)
# Looks like we have a 1D array as of now. Let's do the same example with 2D array and see how it changes the output.

np.random.seed(101)
mynewdata =np.random.randint(0,100,(4,3))
mynewdf = pd.DataFrame(data=mynewdata, index=myIndex, columns=['col1','col2','col3'])
print(mynewdf)

mynewdf.info() #This will print the information about the DataFrame such as the number of entries, the number of columns, the data types of the columns, and the memory usage of the DataFrame. This is a useful method to get a quick overview of the structure and contents of the DataFrame.

# Another method of creating dataframe is by using a dictionary of lists. The keys of the dictionary will become the column names of the DataFrame and the values of the dictionary will become the values of the columns in the DataFrame. The index of the DataFrame will be the default numeric index starting from 0.
mydict = {'col1': [10,20,30,40], 'col2': [50,60,70,80], 'col3': [90,100,110,120]} #This will create a dictionary with the keys as 'col1','col2','col3' and the values as lists of integers.
mydf2 = pd.DataFrame(mydict) #This will create a DataFrame object from the dictionary. The keys of the dictionary will become the column names of the DataFrame and the values of the dictionary will become the values of the columns in the DataFrame. The index of the DataFrame will be the default numeric index starting from 0.  
print(mydf2)

# How do we read file form csv  or excel into dataframe?
df_orders = pd.read_csv('files/orders.csv')
print(df_orders.head(5))

# https://github.com/alpha-nero1/2021-Python-for-Machine-Learning-Data-Science-Masterclass/tree/master This repo has all the lessons from the udemy course "2021 Python for Machine Learning & Data Science Masterclass" by Frank Kane. The exercises that I am working on follows the course. 

# LEt's look at some of the attribiutes that we can call directly on dataframe objects. 

df_orders.columns #This will print the column names of the DataFrame which are 'order_id', 'customer_id', 'order_date', 'order_status', 'order_amount'
print(df_orders.columns) #Reports back actual columns from df

print(df_orders.index) #This will print the index of the DataFrame which is a RangeIndex(start=0, stop=10000, step=1) meaning it starts from 0 and goes up to 9999 with a step of 1. This is the default index for a DataFrame when we do not provide an index. It is a range of integers that starts from 0 and goes up to n-1 where n is the number of rows in the DataFrame. In this case, since there are 10000 rows in the DataFrame, the index goes from 0 to 9999. If there ar labelled index, then it will print the labels of the index instead of the default numeric index.

#strings are objects in dataframe
# integer are int64 objects in dataframe
# float are float64 objects in dataframe

print(df_orders.describe()) #This will print the summary statistics of the DataFrame such as count, mean, std, min, 25%, 50%, 75%, and max for each column in the DataFrame. This is a useful method to get a quick overview of the distribution and central tendency of the data in the DataFrame. It only works for numeric columns in the DataFrame. If we want to get the summary statistics for all columns including non-numeric columns, we can use the include='all' parameter in the describe() method. For example, df_orders.describe(include='all') will give us the summary statistics for all columns in the DataFrame including non-numeric columns.

#The reason we call describe with a parenthesis but not columns or index is because describe is a method of the DataFrame object, while columns and index are attributes of the DataFrame object. Methods are functions that are associated with an object and can be called on that object, while attributes are values that are associated with an object and can be accessed directly without calling them as a function. Therefore, we need to call describe with a parenthesis to execute the method and get the summary statistics of the DataFrame, while we can access columns and index directly without calling them as a function to get the column names and index of the DataFrame respectively.

print(df_orders.describe().transpose())