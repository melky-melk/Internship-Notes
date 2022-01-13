import pandas as pd

df = pd.read_csv('datasets/Pokemon.csv')

df.to_csv('datasets/modified.csv')

new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
