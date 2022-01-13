import pandas as pd
import re

df = pd.read_csv('datasets/Pokemon.csv')

#the ~ in front is the not symbol that removes, without it it would only get all of the mega
new_df = df.loc[~df['Name'].str.contains('Mega', regex = True)]

#the ~ in front is the not symbol that removes, without it it would only get all of the mega

#flags=re.I ignores the case, finds any strings that have fire or grass as type 1 
new_df = df.loc[~df['Type 1'].str.contains('fire|grass', flags=re.I, regex = True)]

# names that begin with pi, ^ is begins with, then any letter a through z, for as many characters
new_df = df.loc[~df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex = True)]


