# #regular Python code

# import csv

# def calculate_rating_stats(data, industry=None):
#     ratings = []
#     for row in data:
#         if row[3]!='NULL' and (not industry or row[1]==industry):
#             ratings.append(float(row[3]))
#     max_rating = max(ratings)
#     min_rating = min(ratings)
#     avg_rating = sum(ratings) / len(ratings)
#     return max_rating, min_rating, avg_rating

# #'w' mode overwrites the file, 'a' appends it, 'r' reads it

# with open("/Users/rohansaxena/Desktop/AI Engineer/Week 12 - Numpy, Pandas, Data Visualization/movies.csv") as f:
#     data = list(csv.reader(f))
#     header = data[0]
#     data = data[1:]
    
#     max_rating, min_rating, avg_rating = calculate_rating_stats(data)
#     print(f"All records: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")
    
#     max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Bollywood")
#     print(f"Bollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")
    
#     max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Hollywood")
#     print(f"Hollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")


import pandas as pd

df = pd.read_csv("/Users/rohansaxena/Desktop/AI Engineer/Week 12 - Numpy, Pandas, Data Visualization/pandas_chapter_3_assets/1_intro/movies.csv")
# print(df.head(7))
# print(df.tail(7))
# print(df.sample(4))
# print(df[2:6])
# print(df.shape)
print(df.imdb_rating.min(),df.imdb_rating.max(),df.imdb_rating.mean())

df2 = df[df.industry=="Bollywood"]

print(df2.imdb_rating.min(),df2.imdb_rating.max(),df2.imdb_rating.mean())

df3 = df[df.industry=="Hollywood"]

print(df3.imdb_rating.min(),df3.imdb_rating.max(),df3.imdb_rating.mean())