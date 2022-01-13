import pandas as pd

df = pd.read_csv('datasets/Pokemon.csv')

# locates it on something other than index
# gets all the fire types
print(df.loc[df['Type 1'] == "Fire"])

print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')])

#gives the mean, standard deviation, quartiles to quickly look at the data
print(df.describe())

# can sort the values
df.sort_values('Name', ascending = False)

# Type 1 will go through a to Z HP will go from high to low
df.sort_values(['Type 1', 'HP'], ascending = [1, 0])