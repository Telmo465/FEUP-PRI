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
final = pd.merge(imdb_platforms, rotten, on=['movie_title', 'year']).drop_duplicates(subset=['review_content'], keep='first')



final.to_csv("datasets/final.csv")






















