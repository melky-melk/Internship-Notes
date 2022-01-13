import pandas as pd

df = pd.read_csv('datasets/Pokemon.csv')

df.to_csv('datasets/modified.csv')

new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]

# removes all of the pokemon whos name contains the word mega

#the ~ in front is the not symbol that removes, without it it would only get all of the mega
new_df = df.loc[~df['Name'].str.contains('Mega')]

# when you shrink the size of the data frame the indexes may start at different place, and will jump around

#to make the index back to normal so its numbered 0,1,2,3 use reset index
new_df.reset_index(drop = True, inplace = True)

new_df.to_csv('datasets/filtered.csv')

