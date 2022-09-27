import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import seaborn as sb

###########################
#load the data from imdb

rawdata_imdb_movies = pd.read_csv("datasets/IMDb_movies.csv")
col_list = ["title", "year", "genre", "director", "description", "actors", "avg_vote", "votes"]
imdb_movies = pd.read_csv("datasets/IMDb_movies.csv", usecols=col_list)

##################################
#load the data from rottentomatoes

#movies
rawdata_rotten_movies = pd.read_csv("datasets/rotten_tomatoes_movies.csv") #movies
# col_list_rt_m = ["movie_title",... ]  #select columns 
# rotten_movies = pd.read_csv("datasets/rotten_tomatoes_movies.csv", usecols=col_list)


#reviews
rawdata_rotten_reviews = pd.read_csv("datasets/rotten_tomatoes_critic_reviews.csv")
# col_list_rt_r = ["movie_title", ...]  #select columns
# rotten_reviews = pd.read_csv("datasets/rotten_tomatoes_critic_reviews.csv", usecols=col_list)


#########statistics#################
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


