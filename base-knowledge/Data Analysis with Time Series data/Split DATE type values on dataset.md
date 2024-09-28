#Codes #pandas #data 

![[Pasted image 20240926120331.png]]
<font color="#f79646">split date to year, month, weekday name column</font>

```Python
import pandas as pd

dataset_path = './opsd_germany_daily.csv'
opsd_daily = pd.read_csv(dataset_path, parse_dates=True, index_col=0)

opsd_daily['Years'] = opsd_daily.index.year # pyright: ignore[]
opsd_daily['Month'] = opsd_daily.index.month # pyright: ignore[]
opsd_daily['Weekday name'] = opsd_daily.index.day_name() # pyright: ignore[]

print(opsd_daily)
```