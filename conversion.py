import csv
import pandas as pd

df=pd.read_csv('dwarf_stars.csv')
#print(df.head())
#print(df.columns)
#print(df.dtypes)
df=df.dropna()
#print(df.head())

df['Radius']=0.102763*df['Radius']
#print(df['Mass'])

df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
#print(df.dtypes)
df['Mass']=0.000954588*df['Mass']
#print(df.columns)

df.drop(['Unnamed: 0'],axis=1,inplace=True)
#print(df.columns)
print(df.head)

df.reset_index(drop=True,inplace=True)
print(df.head)

df.to_csv('unitConversion.csv')