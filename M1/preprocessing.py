import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import seaborn as sb
from functools import reduce


from movies import rotten_movies, rotten_reviews
from platforms import platforms


rotten = pd.merge(rotten_movies, rotten_reviews, on='rotten_tomatoes_link').drop('rotten_tomatoes_link', axis=1)
movies_and_reviews = pd.merge(platforms, rotten, on=['movie_title', 'year']).drop_duplicates(subset=['review_content'], keep='first')
movies_and_reviews.to_csv("datasets/movies_and_reviews.csv")


'''
dic = {}

for original_title in rotten_imdb["original_title"].sample(n=100):
    if original_title not in dic.keys():
        dic[original_title] = 1
    else:
        dic[original_title] += 1


plt.figure(figsize=(50, 10))
plt.xticks(rotation='vertical')
plt.bar(list(dic.keys()),list(dic.values()))
plt.show()

'''

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


