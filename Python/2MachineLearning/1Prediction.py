import pandas as pd
# the python library for machine learning
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('datasets/music.csv')

x = music_data.drop(columns=['genre']) # x is all of the music data that is not the genre
y = music_data['genre'] # y is just the genre information

model = DecisionTreeClassifier()
model.fit(x,y)

print(music_data)