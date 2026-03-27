#Handling missing datas. 

import pandas as pd

df_orders = pd.read_csv(r'files/orders.csv')
print(df_orders.head(5))
                        
# Missing data in pandas are represented as NaN values. 
# Null timestamps are now represented as NaT in pandas. 

# Many methods does not support NaN so we need to handle it hence we need handling techniques. 

# We can also drop of remove the missing data. but this can lead to potential loss of data or information.

# When should we drop a row vs drop a column?

#np.nan is used to display null value
# pd.NA can also be used

# pd.NAT to represent timestamps.

# np.nan is not equal to np.nan so np.nan == np.nan returns false

# HEnce do not use equality, rather write it like "np.nan is np.nan" this way it returns true.
#e.g.,
import numpy as np
myvar = np.nan

print(myvar is np.nan)

# Let's read a file with empty values. 
import pandas as pd
#pd.read_csv
# We will then deal with the missing values. 