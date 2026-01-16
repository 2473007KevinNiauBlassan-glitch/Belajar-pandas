import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#25 Pengaturan tampilan (display option) pada phyton pandas
df= pd.read_csv('./data/titanicfull.csv')
df

pd.set_option('display.max_rows', 5)
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_colwidth', 20)
df

pd.reset_option('^display.', silent=True)
df

pd.describe_option()

pd.set_option('display.max_rows', 7)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_colwidth', 20)
df

pd.reset_option('^display.', silent=True)
df

pd.describe_option()

#26 Membuat Data Frame dari hasil seleksi spreadsheet
df=pd.read_clipboard()
df

#27 Mengenal fungsi agregasi first() dan last()
d= {'dokter':['Budi', 'Wati', 'Iwan', 'Budi', 'Budi', 'Wati'],
    'pasien':['Abdul', 'Rahmat', 'Asep', 'Joko', 'Wiwin', 'Lisa']}
df=pd.DataFrame(d)
df

df.groupby('dokter')['pasien'].count().to_frame()
df.groupby('dokter')['pasien'].first().to_frame()
df.groupby('dokter')['pasien'].last().to_frame()

#28 Mengenal explode dan implode list pada data frame
d= {'Team':['DC', 'Marvel'],
    'Heroes':[['Batman', 'Superman', 'Wonder Woman', 'Aquaman', 'Green Lantern', 'Shazan'],
              'Iron Man', 'Captain America', 'Ant-Man', 'Black Panther', 'Captain Marvel']}
df=pd.DataFrame(d)
df

#Explode
df1=df.explode('Heroes')
df1

d={'Team': ['DC', 'Marvel']}
df2=pd.DataFrame(d)
df2

df2['Imploded']=df1.groupby(df1.index)['Heroes'].agg(list)
df2
