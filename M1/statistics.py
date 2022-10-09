import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import seaborn as sb
from functools import reduce
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from movies import rotten_movies, rotten_reviews
from platforms import imdb_platforms


rotten = pd.merge(rotten_movies, rotten_reviews, on='rotten_tomatoes_link').drop('rotten_tomatoes_link', axis=1)
final = pd.merge(imdb_platforms, rotten, on=['movie_title', 'year'])


####################################


#wordcloud movie descriptions
# text = " ".join(final["movie_info"])
# wordcloud = WordCloud(background_color="white").generate(text)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.savefig('statistics/movie_description_wordcloud.png')
# plt.show()


# # wordcloud movie reviews
# text = " ".join(final["review_content"])
# wordcloud = WordCloud(background_color="white").generate(text)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.savefig('statistics/movie_review_wordcloud.png')
# plt.show()


# # platforms distribution
# platforms = ["Netflix", "Amazon", "Hulu", "Disney+" ]
# availability = [0,0,0,0]
# availability[1] = sum(final["available_amazon"])
# availability[0] = sum(final["available_netflix"])
# availability[3] = sum(final["available_disney"])
# availability[2] = sum(final["available_hulu"])
# plt.pie(availability, labels=platforms, autopct='%1.1f%%')
# plt.savefig('statistics/platforms.png')
# plt.show()



#genre distribution
# all_genres = []

# for genre in final["genre"]:
#     list_genres = genre.split(",")
#     list_genres = list(map(lambda x: textwrap.shorten(x.strip(), width=20), list_genres))
#     all_genres += list_genres
# genre_count = {x: all_genres.count(x) for x in list(set(all_genres))}
# names = list(genre_count.keys())
# values = list(genre_count.values())
# plt.xticks(rotation='vertical')
# plt.ylabel("Number of movies", fontdict={'fontsize': 10, 'fontweight': 'bold'})
# plt.xlabel("Genre", fontdict={'fontsize': 10, 'fontweight': 'bold'})
# plt.bar(range(len(genre_count)), (values), tick_label=names)
# # ax = final.plot(x=names, y=values, kind='bar', legend=False, rot=0)
# # ax.bar_label(ax.containers[0], label_type='edge')
# plt.tight_layout()
# plt.savefig('statistics/genres.png')





#distribution of avg vote imdb
# sb.distplot(a=imdb_platforms.avg_vote)
# plt.savefig('statistics/avg_vote_imdb.png')
# plt.show()


#distribution of avg vote rotten
# sb.distplot(a=rotten_movies.tomatometer_rating)
# plt.savefig('statistics/avg_vote_rotten.png')
# plt.show()

#year distribution of movies
# sb.distplot(a=imdb_platforms.year)
# plt.savefig('statistics/years.png')
# plt.show()



