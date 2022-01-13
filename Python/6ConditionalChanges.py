import pandas as pd

df = pd.read_csv('datasets/Pokemon.csv')

#---------------------------------------RENAMING THINGS-----------------------------------

#goes through type 1, finds fire, and renames it to flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'


#goes through type 1 pokemon, finds the fire types, goes to their legendary attribute, changes it to true
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True


#if the total is greater than 500, then the generation and the legendary, should say TEST VALUE
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST VALUE']
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']