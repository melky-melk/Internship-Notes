import pandas as pd

df = pd.read_csv('datasets/Pokemon.csv')

# groups all the type 1 pokemon, gets the mean and sorts the values from teh highest totals to the lowest
df.groupby(['Type 1']).mean().sort_values('Total', ascending = False)

df.groupby(['Type 1']).sum

#makes a new column
df['count'] = 1
#counts all the types of pokemon, and just gets the count column
print(df.groupby(['Type 1']).count()['count'])