import pandas as pd
from movies import imdb_movies


def open_refine_plataforms_dataframes(file_path):
    
    platform = pd.read_csv(file_path, usecols=["show_id", "title", "release_year"])
    
    platform = platform.assign(movie_title=platform['title'])
    platform = platform.dropna(how='any', axis=0)
    platform['movie_title'] = platform['movie_title'].replace(r'[^A-Za-z0-9/]', '', regex=True)
    platform['movie_title'] = platform['movie_title'].str.lower()

    return platform



def merge_and_add_available_plataforms_column(imdb_movies, platform, columnName):
    
    platform = pd.merge(imdb_movies, platform, on='movie_title', how="left")
    
    
    available_plat = []
    for show_id in platform['show_id'].values:
        available_plat.append(show_id == show_id)
    
    
    imdb_movies[columnName] = pd.Series(available_plat)
    
    return imdb_movies


hulu = open_refine_plataforms_dataframes('datasets/platforms/hulu_titles.csv')
amazon = open_refine_plataforms_dataframes('datasets/platforms/amazon_prime_titles.csv')
disney = open_refine_plataforms_dataframes('datasets/platforms/disney_plus_titles.csv')
netflix = open_refine_plataforms_dataframes('datasets/platforms/netflix_titles.csv')


imdb_movies = merge_and_add_available_plataforms_column(imdb_movies, hulu, 'available_hulu')
imdb_movies = merge_and_add_available_plataforms_column(imdb_movies, amazon, 'available_amazon')
imdb_movies = merge_and_add_available_plataforms_column(imdb_movies, disney, 'available_disney')
imdb_platforms = merge_and_add_available_plataforms_column(imdb_movies, netflix, 'available_netflix')







