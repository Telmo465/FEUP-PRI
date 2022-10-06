import pandas as pd


def rename_columns(movies, originalName, newName):
    
    movies.rename(columns={originalName: newName}, inplace=True)


def read_refine_review_websites(filePath, colList, mergeCol, rename, oldColName, newColName):
    
    movies = pd.read_csv(filePath, usecols=colList)
    movies = movies.dropna(how='any', axis=0)
    
    if rename:
        rename_columns(movies, oldColName, newColName)
    
    movies[mergeCol] = movies[mergeCol].str.lower()
    movies[mergeCol] = movies[mergeCol].replace(r'[^A-Za-z0-9/]', '', regex=True)
    
    return movies



colList = ["title", "original_title", "year", "genre", "director", "description", "actors", "avg_vote", "votes"] 
imdb_movies = read_refine_review_websites("datasets/IMDb_movies.csv", colList, 'movie_title', True, 'title', 'movie_title')  


colList = ["rotten_tomatoes_link", "movie_title", "movie_info", "original_release_date", "tomatometer_count", "tomatometer_rating", "audience_rating"]
rotten_movies = read_refine_review_websites("datasets/rotten_tomatoes_movies.csv", colList, 'movie_title', True, 'original_release_date', 'year')
rotten_movies['year'] = rotten_movies['year'].str[0:4]
rotten_movies["year"] = pd.to_numeric(rotten_movies["year"])

colList = ["rotten_tomatoes_link", "review_content"]  #select columns
rotten_reviews = pd.read_csv("datasets/rotten_tomatoes_critic_reviews.csv", usecols=colList)
rotten_reviews = rotten_reviews.dropna(how='any', axis=0)




