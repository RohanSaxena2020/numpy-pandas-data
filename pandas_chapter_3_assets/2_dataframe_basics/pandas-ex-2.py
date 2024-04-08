import pandas as pd

df = pd.read_csv("/Users/rohansaxena/Desktop/AI Engineer/Week 12 - Numpy, Pandas, Data Visualization/pandas_chapter_3_assets/2_dataframe_basics/movies.csv")
# print(df.head(3))

# print(df.industry.unique())

# print(df.language.unique())

# print(df.industry.value_counts())
# print(df.language.value_counts())

df_2 = df[["title","imdb_rating","industry"]]

print(df_2.head)

df_3 = df[(df.release_year>=2000) & (df.release_year<=2010)]

print(df_3.head)

print(df[df.studio=='Marvel Studios'])

print(df.describe())

print(df.info())

print(df[(df.imdb_rating==df.imdb_rating.max()) | (df.imdb_rating==df.imdb_rating.min())])

df["age"] = df["release_year"].apply(lambda x: 2024-x)
print(df.head(4))

df["profit"] = df.apply(lambda x: x["revenue"] - x["budget"], axis=1)
print(df.head(4))

print(df.index)

df.set_index("title",inplace=True)
print(df.head(4))
print(df.index)

print(df.loc[["Pather Panchali", "Doctor Strange in the Multiverse of Madness"]])

print(df.iloc[0])

print(df.iloc[2:6])


df.reset_index(inplace=True)
print(df.head(4))
