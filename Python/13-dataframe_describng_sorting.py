import pandas as pd

df_orders = pd.read_csv('files/orders.csv') 
print(df_orders.head(5))

print(df_orders.sort_values('Country')) # Note that here we are passing the column name into the function argument hence we are not using the upper bracket otherwise we make use of small bracket. 

print(df_orders.sort_values('Country',ascending=True))
print(df_orders.sort_values('Country',ascending=False))
print(df_orders.sort_values(by=['Country','Price'],ascending=True)) # If we want to give multiple columns into the value argument. 

#Grab index location of min and max values. 
df_orders['Price'].max()
df_orders['Price'].min()

#If we want Index location of the min and max values then 
df_orders['Price'].idxmax()
print("The Index position of the maximum cell element is:", df_orders['Price'].idxmax())

print("\n")
print(df_orders.iloc[df_orders['Price'].idxmax()])

#Correlation
print(df_orders[['Price','Quantity']].corr()) #only works with numeric column.

print(df_orders['Country'].value_counts())  #Tells me value per group

#Similarly we have unique and nunique method
print(df_orders['Country'].unique()) #Returns all the unique names present within the dataset column. 

print(df_orders['Country'].nunique())  #Returns the number of unique values. Total 28 different countries. So we have 28 unique values. 

#Replace method
print(df_orders['Country'].replace('India','IN'))
print(df_orders['Country'].replace(['India','UK'],['IN','United Kingdom']))  #Also takes a list of values. 

#We can easily replace null with zeros using replace method. 

# Let's now look at Map method
# Here first step is to create Map dictionary instead of list and then we pass it to the df

map_dict = {'India': 'IN','Italy':'ITA'}
print(df_orders['Country'].map(map_dict))

df_orders['Country'] = df_orders['Country'].map(map_dict)
print(df_orders.head(10))
# For all the countries that are not defined inside the Map method, values are comign as NaN.
# For all the rest it will replace. OVerall we can say that if we were to replace only a few values we make use of replace method otherwise we make use of Map method. 

# How to deal with duplicated rows
print(df_orders.duplicated()) #Help us with duplicated rows returns the first instance of the duplicated row

print(df_orders[df_orders['Price'].between(50,100,inclusive='both')]) #get me all the prices between 10 and 20 dollars inclusive

#Grab nth largest or nth smallest.
# if we say 10 largest PRices then we make use of nlargest
print(df_orders['Price'].nlargest(10))

print(df_orders.nlargest(10,'Price')) #Essentially this sorts first 10 values and then calls in the head.

print(df_orders.nlargest(10,'Price').iloc[0:2,:])  # we could write iloc here as iloc[0:2,] and it would result in the same. 

#Sample 5 random rows from my df.
print(df_orders.sample(5))

#Sample 10% of my data
print(df_orders.sample(frac=0.1)) #Comes off real handy. It grabs 10% of rows from our df randomly. 