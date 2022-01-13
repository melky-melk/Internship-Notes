import pandas as pd

df = pd.read_csv('datasets/Pokemon.csv')

# makes a new column in the dataframe called total that adds all of their states together
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df = df.drop(columns = ['Total'])

#integer location, colon means all rows 4th column to all the rows in the 9th column. 
# so its all of the stats added together. axis must be 1 so it is horozontal adding 
df['Total'] = df.iloc[:, 4:10].sum(axis = 1)

#to move the total to the right of speed

#instead of manually adding it like this
#df = df['Name','Type1','Type2','HP','Attack','Defense','Sp.Atk','Sp.Def','Speed','Total','Generation']

cols = list(df.columns.values) #gets the names of the columns
# but be careful with hardcoding numbers
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]


print(df.head(6))