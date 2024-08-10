import numpy as np
import pandas as pd
from numpy.random import randn


# creating dataframe
np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E',], ['W','X','Y','Z'])

# Choose specific columns
# print(df[['W', 'Y']])

# add new column
# df['new'] = df['X'] + df['Z']

# delete a column, using axis 0
# df.drop('new', axis=0, inplace=True)

# delete a row, using axis 1
# df.drop('E', axis=1, inplace=True)

# fetch row on the basis of row name
# row = df.loc['C']

# fetch row on the basis of row's index
# indexRow = df.iloc[2]

# fetching subsets of dataframe
# row = df.loc['B', 'Y']

# fetching multiple subsets of dataframe
# row = df.loc[['A', 'B'], ['X', 'Y']] 
# booldf = df>0

print(df)
print(df[df>0])
