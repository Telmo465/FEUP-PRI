import pandas as pd


from movies import rotten_movies, rotten_reviews
from platforms import imdb_platforms


rotten = pd.merge(rotten_movies, rotten_reviews, on='rotten_tomatoes_link').drop('rotten_tomatoes_link', axis=1)
movies_and_reviews = pd.merge(imdb_platforms, rotten, on=['movie_title', 'year']).drop_duplicates(subset=['review_content'], keep='first')
movies_and_reviews.to_csv("movies_and_reviews.csv")


file1 = open("lol.txt", "w")
movies = []

for i in movies_and_reviews.index:
    string = movies_and_reviews['genre'][i].replace(" ", "")   
    lista = string.split(',')
    if 'Adventure' in lista and movies_and_reviews['original_title'][i] not in movies:
        file1.writelines(movies_and_reviews['original_title'][i] + '\n')
        movies.append(movies_and_reviews['original_title'][i])
        




