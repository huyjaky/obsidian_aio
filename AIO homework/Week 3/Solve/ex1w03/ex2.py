import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataset_path = "./opsd_germany_daily.csv"

# NOTE: parse_dates used for date for every column have date in dataset
opsd_daily = pd.read_csv(dataset_path, parse_dates=True, index_col=0)

# NOTE: create new column from properties 
opsd_daily["Years"] = opsd_daily.index.year  # pyright: ignore[]
opsd_daily["Month"] = opsd_daily.index.month  # pyright: ignore[]
opsd_daily["Weekday name"] = opsd_daily.index.day_name()  # pyright: ignore[]
