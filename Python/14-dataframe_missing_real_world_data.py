#Handling missing datas. 

import pandas as pd

df_orders = pd.read_csv(r'files/orders.csv')
print(df_orders.head(5))
                        
# Missing data in pandas are represented as NaN values. 
# Null timestamps are now represented as NaT in pandas. 

# Many methods does not support NaN so we need to handle it hence we need handling techniques. 

# We can also drop of remove the missing data. but this can lead to potential loss of data or information.

# When should we drop a row vs drop a column?
