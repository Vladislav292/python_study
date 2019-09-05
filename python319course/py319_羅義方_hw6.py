import pandas as pd
data= pd.read_csv('stores_old.csv',encoding='big5')
print(data.head())
data=data[['sid','name','tel','wifi']]
print(data.head())
data.to_csv('stores_new.csv',encoding='big5')
