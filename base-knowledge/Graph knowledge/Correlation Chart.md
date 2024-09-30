#correlation #Graph #seaborn 

![[Pasted image 20240928203218.png]]

Tìm mối quan hệ giữa các tag như HUFL, HULL, ... 
xem tỷ lệ liên quan của chúng như thế nào 

```Python
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='viridis', linewidths=0.5)
```


