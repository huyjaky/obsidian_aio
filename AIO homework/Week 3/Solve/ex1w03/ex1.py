import pandas as pd

dataset_path = "./IMDB-Movie-Data.csv"
data = pd.read_csv(dataset_path, index_col="Title")

print(
    data.groupby('Director')[['Rating']].mean().sort_values('Rating',ascending=False).head()# pyright: ignore[]
)




