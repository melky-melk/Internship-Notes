import pandas as pd

df = pd.read_csv('datasets/Pokemon.csv')

# df_xlsx = pd.read_excel('pokemon_data.xslx')
# df = pd.read_csv('pokemon_data.txt')

# just the headers
print(df.columns)

#reads the first 6 records in the file
print(df.head(6))

#read each column
print(df['Name']) # goes through the dictionary, and prints all
print(df['Name'][0:5]) # gets the first 5

print(df.Name) # also works

print(df[['Name', 'Type 1', 'HP']])

#prints the first 4
print(df.head(4))

#gets specifically the location of the second record in the list and prints all of its information
print(df.iloc[1]) 

# gets the second row of the first column
print(df.iloc[2,1])


#iterating through the rows and only printing the names
for index, row in df.iterrows():
	print(index, row['Name'])