import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#05 Membalik urutan baris dan kolom pada data frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.radint(1,10,size=(n_rows, n_cols)),
     colums=cols)
df

#Membalik urutan kolom
df.loc[:, ::-1]

#Membalik urutan baris
df.loc[::-1]
df.loc[::-1, :]

#Membalik urutan baris dan melakukan penyesuaian ulang index
df.loc[::-1].reset_index(derop=True)

#06 Mengganti nama (label) kolom pada Data frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.radint(1,10,size=(n_rows, n_cols)),
     colums=cols)
df

df.rename(columns={'C': 'hobi'})
df.rename(columns={'A':'Nama', 'B': 'Alamat', 'D':'Kota'})

#07 Menghapus(drop) missing values(NaN)
df= pd.util.testing.makeMissingDataframe().reset_index()
df.head()
df= df.rename(columns={'index':'z'})
df.head()
df_backup=df.copy(deep=True)

#menghapus (dorp) setiap kolom yang mengandung missing values
df=df.dropna(axis='columns')
df.head()

df=df_backup.copy(deep=True)
df=df.dropna(axis='rows')
df.head()

#Persentase missing values untuk tiap kolom
df=df_backup.copy(deep=True)
df.isna().mean()

#Menghapus (drop) setiap kolom yang mengandung missing values berdasarkan threshold
treshold=len(df)*0.9
df=df.dropna(tres=treshold,axis='columns')
df.head()

#Presenstase missing values untuk tiap kolom
df = df_backup.copy(deep=True)
df.isna().mean()

#08 Memeriksa kesamaan antar dua buah kolom (series) pada Data Frame
data={'A':[15,15,18, np.nan,12],
      'B':[15,15,18, np.nan,12]}
df=pd.DataFrame(data)
df

#Mengenal pandas series
df['A']
type(df['A'])
type(df)

#Persiapan data frame
data={'A':[15,15,18, np.nan,12],
      'B':[15,15,18, np.nan,12]}
df=pd.DataFrame(data)
df

#Memeriksa kesamaan dengan operator ==
df['A'] == df['B']

#Memeriksa kesamaan dengan method equals()
df['A'].equals(df['B'])

#Memeriksa kesamaan antar dua data frame
df1=df.copy(deep=True)
df.equals(df1)
df==df1