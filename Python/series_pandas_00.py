# We will learn Pandas in this tutorial. Pandas is a powerful library in Python that is used for data manipulation and analysis. It provides data structures like Series and DataFrame which are built on top of numpy arrays and are designed to handle tabular data with ease.    
import pandas as pd

#Pandas uses an extremely powerful table object called dataframe which is a 2-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table, or a dictionary of Series objects.

# Pandas Series Object - Series is a data structure in Pandas that holds an array of information along with a named index. The named index allows us to access the data in the Series using labels instead of just integer positions. A Series can hold any data type, including integers, floats, strings, and even other Python objects. It is a one-dimensional array-like object that can be thought of as a column in a spreadsheet or a SQL table.  
# Note: 1D array if we imagine in excel can be a single row or a single column.
# The named index differentiates a series from a single Numpyarray. Formally we can say Series is a One-dimensional ndarraywith axis labels.

# Think of series as holding a Numpy array internally with with an additional column that has labelled index along with numeric index. The numeric index is the default index that starts from 0 and goes up to n-1 where n is the number of elements in the Series. The labelled index is the index that we can assign to the Series and it can be any type of data, such as strings, integers, etc. The labelled index allows us to access the data in the Series using labels instead of just integer positions.

# We will start with various ways to create a Series object in Pandas.  Then we learn about key properties of Series object. Later we learn how to combine series with a shared index to create a tabular data structure called DataFrame. 

# pd.Series() | Data and Index becomes important paramters in this function. 

myIndex = ['a','b','c','d','e'] #This will create a list of labels for the index of the Series
myData = [10,20,30,40,50] #This will create a list of data for the Series
mySeries = pd.Series(data=myData) #This will create a Series object with the data and index provided. The data parameter is used to specify the values of the Series and the index parameter is used to specify the labels for the index of the Series. If we do not provide an index, it will default to a numeric index starting from 0.
print(mySeries) #This will print the Series object which is a one-dimensional array with the index as number from 0 to 4 and the values as 10,20,30,40,50. The index is shown on the left side and the values are shown on the right side.

print(type(mySeries)) 

mySeries1 = pd.Series(data=myData, index=myIndex) #This will create a Series object with the data and index provided. The data parameter is used to specify the values of the Series and the index parameter is used to specify the labels for the index of the Series. If we do not provide an index, it will default to a numeric index starting from 0.
print(mySeries1) #This will print the Series object which is a one-dimensional array with the index as 'a','b','c','d','e' and the values as 10,20,30,40,50. The index is shown on the left side and the values are shown on the right side. Having Index helps me grab the data almost like a dictionary. For example, if I want to grab the value at index 'c', I can do it via below:
print(mySeries1['c'], "----> This will print the value at index 'c' which is 30. This is one of the key features of a Series object, it allows us to access the data using labels instead of just integer positions. This makes it much easier to work with data that has meaningful labels, such as names, dates, etc.")

print("\n")
      
print(mySeries1.c, "----> This will print the value at index 'c' which is 30. This is one of the key features of a Series object, it allows us to access the data using labels instead of just integer positions. This makes it much easier to work with data that has meaningful labels, such as names, dates, etc.")

# ***** print(mySeries1[0]) #Throws an error because the index of the Series is not numeric, it is 'a','b','c','d','e'. Therefore, we cannot access the data using integer positions. We can only access the data using the labels of the index. If we want to access the data using integer positions, we can use the iloc[] method which allows us to access the data using integer positions. For example, if we want to access the first element of the Series, we can do it via below:
print(mySeries1.iloc[0]) #This will print the first element of the Series which is 10. The iloc[] method is used to access the data using integer positions, while the loc[] method is used to access the data using labels of the index. For example, if we want to access the element at index 'c', we can do it via below:
print(mySeries1.loc['c']) #This will print the element at index 'c' which is 30. The loc[] method is used to access the data using labels of the index, while the iloc[] method is used to access the data using integer positions.
print(type(mySeries1)) #This will print the type of the object which is <class 'pandas.core.series.Series'> meaning it is a Series object from the pandas library.

# Other ways of creating a Series.

# We can do it via dictionary as well. The keys of the dictionary will become the index of the Series and the values of the dictionary will become the values of the Series.
myDict = {'a':10,'b':20,'c':30,'d':40,'e':50} #This will create a dictionary with the keys as 'a','b','c','d','e' and the values as 10,20,30,40,50
mySeries2 = pd.Series(myDict) #This will create a Series object from the dictionary. The keys of the dictionary will become the index of the Series and the values of the dictionary will become the values of the Series.
print(mySeries2) #This will print the Series object which is a one-dimensional array with the index as 'a','b','c','d','e' and the values as 10,20,30,40,50. The index is shown on the left side and the values are shown on the right side. This is another way of creating a Series object in Pandas. We can also create a Series object from a list of tuples. The first element of each tuple will become the index of the Series and the second element of each tuple will become the value of the Series.
myListOfTuples = [('a',10),('b',20),('c',30),('d',40),('e',50)] #This will create a list of tuples where each tuple contains an index and a value for the Series.
mySeries3 = pd.Series(dict(myListOfTuples)) #This will create a Series object from the list of tuples. The first element of each tuple will become the index of the Series and the second element of each tuple will become the value of the Series. We are using the dict() function to convert the list of tuples into a dictionary before creating the Series object.
print(mySeries3) #This will print the Series object which is a one-dimensional array with the index as 'a','b','c','d','e' and the values as 10,20,30,40,50. The index is shown on the left side and the values are shown on the right side. This is yet another way of creating a Series object in Pandas. We can also create a Series object from a numpy array. The index of the Series will be the default numeric index starting from 0 and the values of the Series will be the values of the numpy array.
import numpy as np
myNumpyArray = np.array([10,20,30,40,50]) #This will create a numpy array with the values 10,20,30,40,50
mySeries4 = pd.Series(myNumpyArray) #This will create a Series object from the numpy array. The index of the Series will be the default numeric index starting from 0 and the values of the Series will be the values of the numpy array.
print(mySeries4) #This will print the Series object which is a one-dimensional array with the index as number from 0 to 4 and the values as 10,20,30,40,50. The index is shown on the left side and the values are shown on the right side. This is yet another way of creating a Series object in Pandas. We can also create a Series object from a scalar value. The index of the Series will be the default numeric index starting from 0 and the values of the Series will be the scalar value repeated for each index.

print(mySeries4.iloc[0], mySeries4[0], mySeries4.loc[0])  # Here we hae not explicitly stated index so it is default numeric index starting from 0. Therefore, we can access the data using integer positions, labels of the index, or a combination of both. In this case, since the index is numeric and starts from 0, we can access the first element of the Series using iloc[0], [0], or loc[0]. All three will return the same value which is 10. However, if we had a different index, such as 'a','b','c','d','e', we would not be able to access the data using integer positions and we would have to use the labels of the index to access the data.

