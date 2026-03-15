import numpy as np

#In this tutorial we will learn about some basic operations in numpy arrays.
#Creating a numpy array
arr = np.arange(0,11) #This will create a numpy array from 0 to 10 exclusive of 11
print(arr)

arr = arr + 5 #This will add 5 to each element in the array and return a new array with the result.

print(arr) #This will print the new array which is [5,6,7,8,9,10,11,12,13,14,15]
arr1 = arr - 5 #This will subtract 5 from each element in the array and return a new array with the result.
print(arr1) #This will print the new array which is [0,1,2,3,4,5,6,7,8,9,10]

arr + arr1 #This will add the two arrays element-wise and return a new array with the result.
print(arr + arr1) #This will print the new array which is [5,7,9,11,13,15,17,19,21,23,25]
# To do array with array operations, the two arrays must be of the same shape. If they are not of the same shape, numpy will try to broadcast the smaller array to match the shape of the larger array. This is called broadcasting.
arr2 = np.array([1,2,3,4,5]) #This will create a numpy array with the values [1,2,3,4,5]
print(arr2) #This will print the array which is [1,2,3,4,5]
# print(arr + arr2) #This throws an error because the two arrays are not of the same shape. The first array has 11 elements while the second array has 5 elements. However, if we were to add a new axis to the second array, we can make it compatible for broadcasting.  

#  For division by zero numpy handles it differently. It does not throw an error, instead it returns inf (infinity) for positive numbers and -inf (negative infinity) for negative numbers. It does give us a warning that we are dividing by zero, but it does not stop the execution of the program.
print(arr / 0) #This will print [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf] and it will give us a warning that we are dividing by zero.   

# if we try to divide 0 by 0, it will return nan (not a number) because it is an indeterminate form. It will also give us a warning that we are dividing by zero. However if we try to divide a positive number by 0, it will return inf (infinity) and if we try to divide a negative number by 0, it will return -inf (negative infinity). It will also give us a warning that we are dividing by zero.

# This could become a problem because numpy does not stops the program from executing when we divide by zero, it just returns inf or nan. This could lead to unexpected results in our calculations if we are not careful. Therefore, it is important to check for division by zero before performing any division operations in numpy arrays.

# Numpy universal functions (ufuncs) - Along with basic arithmetic operations, numpy also provides a wide range of universal functions (ufuncs) that can be applied element-wise to arrays. These functions include mathematical functions like sin, cos, exp, log, etc. as well as statistical functions like mean, median, std, etc.
print(np.sqrt(arr)) #This will apply the square root function to each element in the array and return a new array with the result.

print(np.log(arr)) #This will apply the natural logarithm function to each element in the array and return a new array with the result. 

# Summary statistics on arrays - Numpy also provides functions to calculate summary statistics on arrays, such as mean, median, standard deviation, etc.

arr.sum() #This will return the sum of all the elements in the array.
print(arr.sum()) #This will print the sum of all the elements in the array which is 110

arr.max() #This will return the maximum value in the array.
print(arr.max()) #This will print the maximum value in the array which is 15    

arr.mean() #This will return the mean (average) value of the elements in the array.
print(arr.mean()) #This will print the mean value of the elements in the array which is 10.0    

arr.var() #This will return the variance of the elements in the array.
print(arr.var()) #This will print the variance of the elements in the array which is 8.0

arr.std() #This will return the standard deviation of the elements in the array.
print(arr.std()) #This will print the standard deviation of the elements in the array which is 2.8284271247461903

# all these are built in functions in numpy and they are optimized for performance, so they are much faster than using a for loop to calculate these statistics on a list of numbers.

# Now let's look at 2 Dimensional arrays and some operations on them.

arr2d = np.arange(0,9).reshape(3,3) #This will create a 2D array with 3 rows and 3 columns with the values from 0 to 8. The reshape() method is used to change the shape of the array. In this case, we are reshaping the array from a 1D array with 9 elements to a 2D array with 3 rows and 3 columns.
print(arr2d) #This will print the 2D array which is [[0,1,2],[3,4,5],[6,7,8]] 

# same thing can be created by another way.

np.array([[0,1,2],[3,4,5],[6,7,8]]) #This will create a 2D array with 3 rows and 3 columns with the values from 0 to 8. We are directly creating a 2D array by passing a list of lists to the np.array() function. Each inner list represents a row in the 2D array.
print(np.array([[0,1,2],[3,4,5],[6,7,8]])) #This will print the 2D array which is [[0,1,2],[3,4,5],[6,7,8]]

# If we were to perform sum operation on this 2D array, the sum method actually takes an optional argument called axis. The axis argument specifies the axis along which the sum is performed. If we do not specify the axis, it will perform the sum on all the elements in the array and return a single value which is the sum of all the elements in the array. However, if we specify the axis, it will perform the sum along that axis and return an array with the result. The axis argument can take the following values:

# axis=0: This will perform the sum along the columns (i.e., it will sum the values in each column and return an array with the result).
# axis=1: This will perform the sum along the rows (i.e., it will sum the values in each row and return an array with the result).

print(arr2d.sum()) #This will print the sum of all the elements in the array which is 36
print(arr2d.sum(axis=0)) #This will print the sum along the columns which is [9,12,15] (0+3+6, 1+4+7, 2+5+8)
print(arr2d.sum(axis=1)) #This will print the sum along the rows which is [3,12,21] (0+1+2, 3+4+5, 6+7+8)       

# KEyword here is "across" which means that we are performing the sum across the columns or across the rows. This is a very powerful feature of numpy arrays and it allows us to perform operations on multi-dimensional arrays in a very efficient way.