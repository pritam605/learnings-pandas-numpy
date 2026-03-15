import numpy as np

my_list = [1, 2, 3]
print(np.array(my_list))

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("My matrix is \n", np.array(my_matrix))

np.zeros(5) 
#Creates an array of zeros with the specified length. 0's are floating point numbers by default. If you want to specify the data type, you can use the dtype parameter. For example, np.zeros(5, dtype=int) will create an array of zeros with integer data type.
print("My zeros array is \n", np.zeros(5))

# If I want a 2 dimensional array of zeros, I can specify the shape as a tuple.
np.zeros((2,3)) #Creates a 2D array of zeros with 2 rows and 3 columns.
# The shape of the array is specified as a tuple (2, 3) where 2 is the number of rows and 3 is the number of columns. The resulting array will have 2 rows and 3 columns filled with zeros.
print("My 2D zeros array is \n", np.zeros((2,3)))

np.arange(0, 10, 2) #Start , Stop and Optional Step size
print("My arange array is \n", np.arange(0, 10, 2)) 
# The last number is not included in the array. It goes up to 10 but does not include 10. It includes 0, 2, 4, 6, 8.
# Also, note that arange has a default step size of 1. So if you just do np.arange(0, 10), it will create an array of numbers from 0 to 9 with a step size of 1.
# It is spelled as arange and not arrange. It is a common mistake to spell it as arrange, but the correct spelling is arange.

np.ones(4) #Creates an array of ones with the specified length. 1's are floating point numbers by default. If you want to specify the data type, you can use the dtype parameter. For example, np.ones(4, dtype=int) will create an array of ones with integer data type.
print("My ones array is \n", np.ones(4,dtype=int))

np.ones((3,4)) #Creates a 2D array of ones with 3 rows and 4 columns.
print("My 2D ones array is \n", np.ones((3,4)))

np.linspace(0, 10, 5) #Start , Stop and Number of points to generate
print("My linspace array is \n", np.linspace(0, 10, 5))
# The linspace function generates a specified number of evenly spaced values between a given start and stop value. 
# In this case, it generates 5 evenly spaced values between 0 and 10, which are 0.0, 2.5, 5.0, 7.5, and 10.0.
# The linspace function is particularly useful when you want to create a range of values that are evenly spaced, regardless of the step size.
# Do not confuse this with arange, which generates values based on a specified step size. Linspace generates values based on the number of points you want to create, while arange generates values based on the step size you specify.
# In linspace the stop value is included in the generated array, while in arange the stop value is not included. This is an important distinction to keep in mind when using these functions.

np.linspace(0,5,21) #This will generate 21 evenly spaced values between 0 and 5, including both 0 and 5. The values will be 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, and 5.0.
print("My linspace array with 21 points is \n", np.linspace(0,5,21))

np.eye(4) #Creates a 2D array with ones on the diagonal and zeros elsewhere. The size of the array is determined by the argument passed to the function. In this case, it creates a 4x4 identity matrix.
print("My identity matrix is \n", np.eye(4))
# np.eye(4) creates a 4x4 identity matrix, which is a square matrix with ones on the main diagonal and zeros elsewhere. The resulting array will have the following structure:
# [[1. 0. 0. 0.]    
#  [0. 1. 0. 0.]    
#  [0. 0. 1. 0.]    
#  [0. 0. 0. 1.]]

np.random.rand(5) #Generates an array of 5 random numbers between 0 and 1. The numbers are drawn from a uniform distribution over [0, 1).
print("My random array is \n", np.random.rand(5))
# The function np.random has lots of functions to generate random numbers. 
# e.g., np.random.randint(0, 10, 5) will generate an array of 5 random integers between 0 and 10 (exclusive). The numbers are drawn from a uniform distribution over the specified range.
# The np.random.rand function generates random numbers between 0 and 1. The argument passed to the function specifies the shape of the output array. In this case, it generates an array of 5 random numbers. If you want to generate a 2D array of random numbers, you can pass a tuple as an argument. For example, np.random.rand(2, 3) will generate a 2x3 array of random numbers between 0 and 1.

# simplest of random function is np.random.rand() which generates a single random number between 0 and 1. 
# If you want to generate an array of random numbers, you can pass the desired shape as an argument to the function. For example, np.random.rand(5) will generate an array of 5 random numbers between 0 and 1, and np.random.rand(2, 3) will generate a 2D array of random numbers with 2 rows and 3 columns.

print(np.random.rand()) #This will generate a single random number between 0 and 1. The number is drawn from a uniform distribution over [0, 1) where 0 is inclusive and 1 is exclusive. The resulting value will be a random floating-point number between 0 and 1.
print("My random array is \n", np.random.rand(5)) #This will generate an array of 5 random numbers between 0 and 1. The numbers are drawn from a uniform distribution over [0, 1). The resulting array will contain 5 random values, each between 0 and 1.
# Also to note that in np.random.rand the distribution is uniform, which means that each number between 0 and 1 has an equal chance of being generated. If you want to generate random numbers from a different distribution, you can use other functions in the np.random module, such as np.random.normal for a normal distribution or np.random.poisson for a Poisson distribution.
# We can also provide the shape of the array inside this function. For example, np.random.rand(2, 3) will generate a 2D array of random numbers with 2 rows and 3 columns, where each number is between 0 and 1. This way of passing arugment is a little different from the way we pass arguments in other functions like np.zeros or np.ones, where we pass the shape as a tuple. In np.random.rand, we pass the dimensions as separate arguments. So np.random.rand(2, 3) is equivalent to np.random.rand((2, 3)) in terms of the shape of the output array.

#Lets look at standard distribution of random numbers.
np.random.randn(5) #Generates an array of 5 random numbers from the standard normal distribution. The numbers are drawn from a normal distribution with mean 0 and standard deviation 1.This means numbers will be centered around 0, and most of the values will fall within the range of -3 to 3. The resulting array will contain 5 random values drawn from this distribution. Reason it choose from -3 to 3 is because in a normal distribution, about 99.7% of the values fall within three standard deviations from the mean. Since the mean is 0 and the standard deviation is 1, most of the values will be between -3 and 3.
print("My standard normal random array is \n", np.random.randn(5))

np.random.randn(2, 3) #Generates a 2D array of random numbers from the standard normal distribution with 2 rows and 3 columns. Each number is drawn from a normal distribution with mean 0 and standard deviation 1. The resulting array will contain 6 random values (2 rows x 3 columns) drawn from this distribution. Notice that unlike last example where range was -3 to 3, here we can have values outside of this range as well, since it is a normal distribution and not a uniform distribution. The values will still be centered around 0, but they can be more spread out compared to the uniform distribution.
print("My 2D standard normal random array is \n", np.random.randn(2, 3))

np.random.randint(0, 10, 5) #Generates an array of 5 random integers between 0 and 10 (exclusive). The numbers are drawn from a uniform distribution over the specified range. The resulting array will contain 5 random integer values, each between 0 and 9.
print("My random integer array is \n", np.random.randint(0, 10, 5))
# The np.random.randint function generates random integers between a specified low (inclusive) and high (exclusive) value. The first argument is the low value, the second argument is the high value, and the third argument is the number of random integers to generate. In this case, it generates 5 random integers between 0 (inclusive) and 10 (exclusive), which means the possible values are 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. The resulting array will contain 5 random integer values drawn from this range.

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("My matrix is \n", np.array(my_matrix))

np.zeros(5) 
#Creates an array of zeros with the specified length. 0's are floating point numbers by default. If you want to specify the data type, you can use the dtype parameter. For example, np.zeros(5, dtype=int) will create an array of zeros with integer data type.
print("My zeros array is \n", np.zeros(5))

# If I want a 2 dimensional array of zeros, I can specify the shape as a tuple.
np.zeros((2,3)) #Creates a 2D array of zeros with 2 rows and 3 columns.
# The shape of the array is specified as a tuple (2, 3) where 2 is the number of rows and 3 is the number of columns. The resulting array will have 2 rows and 3 columns filled with zeros.
print("My 2D zeros array is \n", np.zeros((2,3)))

np.arange(0, 10, 2) #Start , Stop and Optional Step size
print("My arange array is \n", np.arange(0, 10, 2)) 
# The last number is not included in the array. It goes up to 10 but does not include 10. It includes 0, 2, 4, 6, 8.
# Also, note that arange has a default step size of 1. So if you just do np.arange(0, 10), it will create an array of numbers from 0 to 9 with a step size of 1.
# It is spelled as arange and not arrange. It is a common mistake to spell it as arrange, but the correct spelling is arange.

np.ones(4) #Creates an array of ones with the specified length. 1's are floating point numbers by default. If you want to specify the data type, you can use the dtype parameter. For example, np.ones(4, dtype=int) will create an array of ones with integer data type.
print("My ones array is \n", np.ones(4,dtype=int))

np.ones((3,4)) #Creates a 2D array of ones with 3 rows and 4 columns.
print("My 2D ones array is \n", np.ones((3,4)))

np.linspace(0, 10, 5) #Start , Stop and Number of points to generate
print("My linspace array is \n", np.linspace(0, 10, 5))
# The linspace function generates a specified number of evenly spaced values between a given start and stop value. 
# In this case, it generates 5 evenly spaced values between 0 and 10, which are 0.0, 2.5, 5.0, 7.5, and 10.0.
# The linspace function is particularly useful when you want to create a range of values that are evenly spaced, regardless of the step size.
# Do not confuse this with arange, which generates values based on a specified step size. Linspace generates values based on the number of points you want to create, while arange generates values based on the step size you specify.
# In linspace the stop value is included in the generated array, while in arange the stop value is not included. This is an important distinction to keep in mind when using these functions.

np.linspace(0,5,21) #This will generate 21 evenly spaced values between 0 and 5, including both 0 and 5. The values will be 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, and 5.0.
print("My linspace array with 21 points is \n", np.linspace(0,5,21))

np.eye(4) #Creates a 2D array with ones on the diagonal and zeros elsewhere. The size of the array is determined by the argument passed to the function. In this case, it creates a 4x4 identity matrix.
print("My identity matrix is \n", np.eye(4))
# np.eye(4) creates a 4x4 identity matrix, which is a square matrix with ones on the main diagonal and zeros elsewhere. The resulting array will have the following structure:
# [[1. 0. 0. 0.]    
#  [0. 1. 0. 0.]    
#  [0. 0. 1. 0.]    
#  [0. 0. 0. 1.]]

np.random.rand(5) #Generates an array of 5 random numbers between 0 and 1. The numbers are drawn from a uniform distribution over [0, 1).
print("My random array is \n", np.random.rand(5))
# The function np.random has lots of functions to generate random numbers. 
# e.g., np.random.randint(0, 10, 5) will generate an array of 5 random integers between 0 and 10 (exclusive). The numbers are drawn from a uniform distribution over the specified range.
# The np.random.rand function generates random numbers between 0 and 1. The argument passed to the function specifies the shape of the output array. In this case, it generates an array of 5 random numbers. If you want to generate a 2D array of random numbers, you can pass a tuple as an argument. For example, np.random.rand(2, 3) will generate a 2x3 array of random numbers between 0 and 1.

# simplest of random function is np.random.rand() which generates a single random number between 0 and 1. 
# If you want to generate an array of random numbers, you can pass the desired shape as an argument to the function. For example, np.random.rand(5) will generate an array of 5 random numbers between 0 and 1, and np.random.rand(2, 3) will generate a 2D array of random numbers with 2 rows and 3 columns.

print(np.random.rand()) #This will generate a single random number between 0 and 1. The number is drawn from a uniform distribution over [0, 1) where 0 is inclusive and 1 is exclusive. The resulting value will be a random floating-point number between 0 and 1.
print("My random array is \n", np.random.rand(5)) #This will generate an array of 5 random numbers between 0 and 1. The numbers are drawn from a uniform distribution over [0, 1). The resulting array will contain 5 random values, each between 0 and 1.
# Also to note that in np.random.rand the distribution is uniform, which means that each number between 0 and 1 has an equal chance of being generated. If you want to generate random numbers from a different distribution, you can use other functions in the np.random module, such as np.random.normal for a normal distribution or np.random.poisson for a Poisson distribution.
# We can also provide the shape of the array inside this function. For example, np.random.rand(2, 3) will generate a 2D array of random numbers with 2 rows and 3 columns, where each number is between 0 and 1. This way of passing arugment is a little different from the way we pass arguments in other functions like np.zeros or np.ones, where we pass the shape as a tuple. In np.random.rand, we pass the dimensions as separate arguments. So np.random.rand(2, 3) is equivalent to np.random.rand((2, 3)) in terms of the shape of the output array.

#Lets look at standard distribution of random numbers.
np.random.randn(5) #Generates an array of 5 random numbers from the standard normal distribution. The numbers are drawn from a normal distribution with mean 0 and standard deviation 1.This means numbers will be centered around 0, and most of the values will fall within the range of -3 to 3. The resulting array will contain 5 random values drawn from this distribution. Reason it choose from -3 to 3 is because in a normal distribution, about 99.7% of the values fall within three standard deviations from the mean. Since the mean is 0 and the standard deviation is 1, most of the values will be between -3 and 3.
print("My standard normal random array is \n", np.random.randn(5))

np.random.randn(2, 3) #Generates a 2D array of random numbers from the standard normal distribution with 2 rows and 3 columns. Each number is drawn from a normal distribution with mean 0 and standard deviation 1. The resulting array will contain 6 random values (2 rows x 3 columns) drawn from this distribution. Notice that unlike last example where range was -3 to 3, here we can have values outside of this range as well, since it is a normal distribution and not a uniform distribution. The values will still be centered around 0, but they can be more spread out compared to the uniform distribution.
print("My 2D standard normal random array is \n", np.random.randn(2, 3))

np.random.randint(0, 10, 5) #Generates an array of 5 random integers between 0 and 10 (exclusive). The numbers are drawn from a uniform distribution over the specified range. The resulting array will contain 5 random integer values, each between 0 and 9.
print("My random integer array is \n", np.random.randint(0, 10, 5))
# The np.random.randint function generates random integers between a specified low (inclusive) and high (exclusive) value. The first argument is the low value, the second argument is the high value, and the third argument is the number of random integers to generate. In this case, it generates 5 random integers between 0 (inclusive) and 10 (exclusive), which means the possible values are 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. The resulting array will contain 5 random integer values drawn from this range.

np.random.seed(42) #Sets the seed for the random number generator. This ensures that the same sequence of random numbers is generated each time the code is run. The argument passed to the function is an integer that serves as the seed value. By setting the seed, you can reproduce the same random numbers in future runs of the code, which is useful for debugging and testing purposes.
print("My random array with seed 42 is \n", np.random.rand(5)) #This will generate the same array of 5 random numbers between 0 and 1 every time you run the code, because the seed has been set to 42. The numbers are drawn from a uniform distribution over [0, 1). The resulting array will contain the same 5 random values each time you run the code, allowing for reproducibility in your results.

#Another example
np.random.seed(101)
print("My random array with seed 101 is \n", np.random.rand(5)) #This will generate the same array of 5 random numbers between 0 and 1 every time you run the code, because the seed has been set to 101. The numbers are drawn from a uniform distribution over [0, 1). The resulting array will contain the same 5 random values each time you run the code, allowing for reproducibility in your results.

# seed becomes useful when you want to generate random numbers for testing or debugging purposes. By setting a specific seed value, you can ensure that the same sequence of random numbers is generated each time you run the code. This allows you to reproduce the same results and identify any issues or inconsistencies in your code. For example, if you are testing a function that relies on random numbers, setting a seed will help you verify that the function behaves as expected with the same input data.

arr = np.arange(0,30,2) #This will generate an array of numbers starting from 0 up to (but not including) 30, with a step size of 2. The resulting array will contain the values [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28].
arr.reshape(5, 3) #This will reshape the array into a 2D array with 5 rows and as many columns as needed to accommodate all the elements. The -1 in the reshape function tells NumPy to automatically calculate the number of columns based on the total number of elements in the array and the specified number of rows. In this case, since there are 15 elements in the original array and we want 5 rows, NumPy will determine that we need 3 columns to fit all the elements. The resulting array will have the shape (5, 3) and will contain the values:

print("My reshaped array is \n", arr.reshape(5, 3))
# reshape can throw an error if the total number of elements in the original array does not match the total number of elements in the reshaped array. For example, if you try to reshape an array of 10 elements into a shape that requires 12 elements, you will get an error. It is important to ensure that the total number of elements remains the same when reshaping an array. 5 * 3 = 15, which matches the total number of elements in the original array (0 to 28 with a step of 2 gives us 15 elements). If we tried to reshape it into a shape that does not accommodate all 15 elements, we would get an error.

ranarr = np.random.randint(0,101,10)
print("My random integer array between 0 and 100 is \n", ranarr)
ranarr.max() #This will return the maximum value in the array ranarr. The max function scans through all the elements in the array and identifies the largest value. The resulting output will be the maximum integer value present in the ranarr array, which contains 10 random integers between 0 and 100 (inclusive).
print("The maximum value in ranarr is \n", ranarr.max())

ranarr.min() #This will return the minimum value in the array ranarr. The min function scans through all the elements in the array and identifies the smallest value. The resulting output will be the minimum integer value present in the ranarr array, which contains 10 random integers between 0 and 100 (inclusive).
print("The minimum value in ranarr is \n", ranarr.min())

ranarr.argmax() #This will return the index of the maximum value in the array ranarr. The argmax function scans through all the elements in the array and identifies the index of the largest value. The resulting output will be the index position of the maximum integer value present in the ranarr array, which contains 10 random integers between 0 and 100 (inclusive). Note that if there are multiple occurrences of the maximum value, argmax will return the index of the first occurrence. Index starts from 0, so if the maximum value is at the first position in the array, argmax will return 0.
print("The index of the maximum value in ranarr is \n", ranarr.argmax())

ranarr.argmin() #This will return the index of the minimum value in the array ranarr. The argmin function scans through all the elements in the array and identifies the index of the smallest value. The resulting output will be the index position of the minimum integer value present in the ranarr array, which contains 10 random integers between 0 and 100 (inclusive). Note that if there are multiple occurrences of the minimum value, argmin will return the index of the first occurrence. Index starts from 0, so if the minimum value is at the first position in the array, argmin will return 0.
print("The index of the minimum value in ranarr is \n", ranarr.argmin())

arr.shape #This will return the shape of the array arr. The shape attribute provides a tuple that represents the dimensions of the array. In this case, since arr was reshaped to have 5 rows and 3 columns, the resulting output will be (5, 3), indicating that the array has 5 rows and 3 columns. The shape of an array is important for understanding its structure and how it can be manipulated in various operations.
print("The shape of arr is \n", arr.shape)

#Note that arr.shape is an attribute call not a function call, so we do not use parentheses when accessing it. If we were to use parentheses like arr.shape(), it would result in an error because shape is not a function but an attribute of the array object. Always remember to access attributes without parentheses and functions with parentheses in Python. 

# How to remember which one is attribute vs which one is Method?
# In general, attributes are properties of an object that provide information about the object, while methods are functions that perform actions on the object.
# For example, in the case of a NumPy array, shape is an attribute because it provides information about the dimensions of the array, while reshape is a method because it performs an action that changes the structure of the array.

arr.reshape(15,) #This will reshape the array arr into a 1D array with 15 elements. The resulting array will contain the same values as the original array but will be flattened into a single dimension. The output will be an array with the shape (15,) and will contain the values [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]. This is useful when you want to convert a multi-dimensional array into a flat array for certain operations or analyses.
print("My reshaped array into 1D is \n", arr.reshape(15,))

# Or I can reshape arr into 
arr.reshape(1,15) #This will reshape the array arr into a 2D array with 1 row and 15 columns. The resulting array will contain the same values as the original array but will be structured as a single row with 15 columns. The output will be an array with the shape (1, 15) and will contain the values [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]]. This is useful when you want to convert a multi-dimensional array into a specific shape for certain operations or analyses.
print("My reshaped array into 2D with 1 row and 15 columns is \n", arr.reshape(1,15))