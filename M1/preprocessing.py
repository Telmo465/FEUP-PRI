import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import seaborn as sb



###########################
#load the data from imdb

rawdata_imdb_movies = pd.read_csv("datasets/IMDb_movies.csv")
col_list = ["title", "original_title", "year", "genre", "director", "description", "actors", "avg_vote", "votes"]
imdb_movies = pd.read_csv("datasets/IMDb_movies.csv", usecols=col_list)

#rename imdb_movies panda column
imdb_movies.rename(columns={'title': 'movie_title'}, inplace=True)
imdb_movies = imdb_movies.dropna(how='any', axis=0)
#normalize imdb
imdb_movies['movie_title'] = imdb_movies['movie_title'].str.lower()
imdb_movies['movie_title'] = imdb_movies['movie_title'].replace(r'[^A-Za-z0-9/]', '', regex=True)


###########################






##################################
#load the data from rottentomatoes

#movies
rawdata_rotten_movies = pd.read_csv("datasets/rotten_tomatoes_movies.csv") #movies
col_list_rt_m = ["rotten_tomatoes_link", "movie_title", "movie_info", "original_release_date"]  #select columns 
rotten_movies = pd.read_csv("datasets/rotten_tomatoes_movies.csv", usecols=col_list_rt_m)

#reviews
rawdata_rotten_reviews = pd.read_csv("datasets/rotten_tomatoes_critic_reviews.csv")
col_list_rt_r = ["rotten_tomatoes_link", "review_content"]  #select columns
rotten_reviews = pd.read_csv("datasets/rotten_tomatoes_critic_reviews.csv", usecols=col_list_rt_r)

#delete rows with null values
rotten_movies = rotten_movies.dropna(how='any', axis=0)
rotten_reviews = rotten_reviews.dropna(how='any', axis=0)

#normalization
rotten_movies['movie_title'] = rotten_movies['movie_title'].str.lower()
rotten_movies['movie_title'] = rotten_movies['movie_title'].replace(r'[^A-Za-z0-9/]', '', regex=True)

#clean release_date
rotten_movies['original_release_date'] = rotten_movies['original_release_date'].str[0:4]
rotten_movies.rename(columns={'original_release_date': 'year'}, inplace=True)

################################






################################
##########Merge pandas##########

#merge pandas
rotten = pd.merge(rotten_movies, rotten_reviews, on='rotten_tomatoes_link')
rotten_imdb = pd.merge(imdb_movies, rotten, on=['movie_title', 'year']).drop_duplicates(subset=['review_content'], keep='first')

print(rotten_imdb)

rotten_imdb.to_csv("datasets/output.csv")


################################











#################################


#print(merge_df)


#########Statistics#################
# all_genres = []
# for genre in df["genre"]:
#     list_genres = genre.split(",")
#     list_genres = list(map(lambda x: textwrap.shorten(x.strip(), width=20), list_genres))
#     all_genres += list_genres
# genre_count = {x: all_genres.count(x) for x in list(set(all_genres))}
# print((sorted(genre_count.items(), key=lambda x: x[1], reverse=True)))
# names = list(genre_count.keys())
# print(names)
# values = list(genre_count.values())
# print(values)
# plt.xticks(rotation='vertical')
# plt.bar(range(len(genre_count)), (values), tick_label=names)
# ax = df.plot(x=names, y=values, kind='bar', legend=False, rot=0)
# ax.bar_label(ax.containers[0], label_type='edge')
# plt.tight_layout()
####################################


