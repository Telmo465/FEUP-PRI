import pandas as pd


from movies import rotten_movies, rotten_reviews
from platforms import imdb_platforms


rotten = pd.merge(rotten_movies, rotten_reviews, on='rotten_tomatoes_link').drop('rotten_tomatoes_link', axis=1)
movies_and_reviews = pd.merge(imdb_platforms, rotten, on=['movie_title', 'year']).drop_duplicates(subset=['review_content'], keep='first')
movies_and_reviews.to_csv("movies_and_reviews.csv")




