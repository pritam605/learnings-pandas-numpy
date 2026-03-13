import numpy as np

#In this tutorial we will learn about indexing and selection in numpy arrays.
#Creating a numpy array
arr = np.arange(0,11) #This will create a numpy array from 0 to 10 exclusive of 11
print(arr)
#Indexing based on how we index in lists
print(arr[8]) #This will print the value at index 8 which is 8
#Slicing
print(arr[1:5], "This will print the values from index 1 to 4 which are 1,2,3,4")
print(arr[:6], "This will print the values from index 0 to 5 which are 0,1,2,3,4,5 meaning 6 is exclusive")
print(arr[5:], "This will print the values from index 5 to the end which are 5,6,7,8,9,10")

#Broadcasting
#In Python lists we can only reassign parts of a list with another list of the same shape and size. In numpy arrays we can reassign parts of an array with a single value and it will broadcast that value to the entire selection.
arr[5:8] = 100 #This will assign the value 100 to the elements at indices 5, 6, and 7
print(arr)

#slicing a section of an array creates a view of the original array, not a copy. This means that if we modify the sliced section, it will affect the original array.
arr_slice = arr[0:6] #This creates a view of the original array from index 0 to 5
print(arr_slice)
print(arr)

#if we were to do arr_slice[:] = 99, it would change the values in the original array as well because arr_slice is a view of the original array.
arr_slice[:] = 99
print(arr_slice)
print(arr) #This will show that the original array has been modified as well because arr_slice is a view of the original array.

#If you do not want to modify the original array, you can create a copy of the sliced section using the copy() method.
arr_slice_copy = arr[0:6].copy() #This creates a copy of the sliced section of the original array from index 0 to 5
arr_slice_copy[:] = 88 #This will modify the copy of the sliced section, not the original array
print(arr_slice_copy)
print(arr)

# Indexing of 2D arrays
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)   

print(arr_2d.shape) #This will print the shape of the 2D array which is (3,3) meaning 3 rows and 3 columns


# If we were to grab the first row of the 2D array, we can do it via below:
print(arr_2d[0]) #This will print the first row which is [1,2,3]

# Now if we want to Index the columns of the specific rows we can do it via below:
print(arr_2d[0][0]) # or arr_2d[0,0] This will print the value at the first row and first column which is 1
print(arr_2d[1][2]) # or arr_2d[1,2] This will print the value at the second row and third column which is 6

print(arr_2d[0:2]) #This will print the first two rows which are [[1,2,3],[4,5,6]]
print(arr_2d[:2]) #This will also print the first two rows which are [[1,2,3],[4,5,6]]
print(arr_2d[1:]) #This will print the last two rows which are [[4,5,6],[7,8,9]]

# Till now we were slicing  either on rows or on columns, but we can also slice on both rows and columns at the same time. For example, if we want to grab the first two rows and the first two columns, we can do it via below:
print(arr_2d[:2,:2]) #This will print the first two rows and the first two columns which are [[1,2],[4,5]]

# lets say we want to print first 2 rows and the last 2 columns, we can do it via below:
print(arr_2d[:2,1:]) #This will print the first two rows and the last two columns which are [[2,3],[5,6]]s

# Most common type of selection used is called "Conditional Selection"
print(arr_2d) #This will print the 2D array which is [[1,2,3],[4,5,6],[7,8,9]]
print(arr_2d > 4) #This will print a boolean array where the values greater than 4 are True and the values less than or equal to 4 are False which is [[False,False,False],[False,True,True],[True,True,True]]
print(arr_2d[arr_2d > 4]) #This will print a numpy arrray with the values that are greater than 4 which are [5,6,7,8,9]

# this is the sort of thing that we use most often and we also use it in pandas dataframes which we will learn in the next tutorial. We can also use multiple conditions for selection. For example, if we want to select the values that are greater than 4 and less than 8, we can do it via below:
print(arr_2d[(arr_2d > 4) & (arr_2d < 8)]) #This will print a numpy array with the values that are greater than 4 and less than 8 which are [5,6,7]     

# If we were to define a numpy array say rolled dice and we want to count the number of instances when the value is greater than 4, we can do it via below:
rolled_dice = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(rolled_dice)
print((rolled_dice > 4).sum()) #This will print the number of instances where the value is greater than 4 which is 5            

#or if we want to make use of what we learned via conditional selection and we want to count the number of instances where the value is greater than 4, we can do it via below:
print(len(rolled_dice[rolled_dice > 4])) #This will also print the number of instances where the value is greater than 4 which is 5 

print(rolled_dice[rolled_dice > 4]) #Irrespective of the shape of rolled_dice_array the conditional selection will return a 1D array with the values that are greater than 4 which are [5,6,7,8,9]  