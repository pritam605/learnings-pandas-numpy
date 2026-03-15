import numpy as np
# Create an array of 10 zeros
np.zeros(10)
print(np.zeros(10)) #This will print an array of 10 zeros which is [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#create an array of 10 ones
np.ones(10) 
print(np.ones(10)) #This will print an array of 10 ones which is [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

#Create an array of 10 fives.
np.ones(10) * 5
print(np.ones(10) * 5) #This will print an array of 10 fives which is [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]   

# create an array of Integers from 10 to 50 
np.arange(10,51) #This will create an array of integers from 10 to 50 exclusive of 51
print(np.arange(10,51)) #This will print an array of integers from 10 to 50 exclusive of 51 which is [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50]

# create an array of all the even integers from 10 to 50
np.arange(10,51,2) #This will create an array of all the even integers from 10 to 50 exclusive of 51. The third argument in the arange() function is the step size, which is 2 in this case, meaning it will skip every other integer.
print(np.arange(10,51,2)) #This will print an array of all the even integers from 10 to 50 exclusive of 51 which is [10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50]

#Imp note below - 
# One thing to note is that if you want to reshape or subset your array lets say by showing first 3 rows and 2nd column from a 5X6 array 
# then in that case, don't do arr([:3,1]) otherwise you will have to reshape it since it gives just one row as output. 
# Instead, do arr[:3,1:2] which will give you the first 3 rows and the 2nd column as a 2D array without the need to reshape it.

