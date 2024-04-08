import pandas as pd

path = "/Users/rohansaxena/Desktop/AI Engineer/Week 12 - Numpy, Pandas, Data Visualization/pandas_chapter_3_assets/3_read_write_to_excel/"

# df1 = pd.read_csv(path+"stock_data.csv",skiprows=1)
# print(df1.head)

# df2  = pd.read_csv(path+"stock_data.csv", header=1)
# print(df2.head)

# df3  = pd.read_csv(path+"stock_data.csv", header=1, names = ["stock_symbol","eps","revenue","price","founder"])
# print(df3.head)

# df4  = pd.read_csv(path+"stock_data.csv", header=1, nrows=3)
# print(df4.head)

# df = pd.read_csv(path+"stock_data.csv", header=1,na_values=['not available',-1,'n.a.'])

# df["pe"] = df["price"]/df["eps"]

# print(df)

# df.to_csv(path+"pe1.csv",index=False)

# df.to_csv(path+"pe2.csv",index=False,header=False)

# df_movies = pd.read_excel(path+"movies_db.xlsx","movies")
# print(df_movies.head(4))

# def standardize_currency(curr):
#     if curr == "$$" or curr == "Dollars":
#         return "USD"
#     return curr


# df_financials = pd.read_excel(path+"movies_db.xlsx","financials",converters= {
#     'currency': standardize_currency
# })

# print(df_financials.head(5))

# df_merged = pd.merge(df_movies,df_financials,on="movie_id")
# print(df_merged)

# df_merged.to_excel(path+"movies_merged_byrohan.xlsx", sheet_name="Sheet1",index=False)

df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

print(df_stocks)

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

print(df_weather)

with pd.ExcelWriter(path+"stocks_weather_byrohan.xlsx") as writer:
    df_stocks.to_excel(writer,sheet_name="stocks")
    df_weather.to_excel(writer,sheet_name="weather")

