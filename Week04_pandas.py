import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Konversi nilai numerik ke dalam sejumlah kategori 
n_rows = 10
n_cols = 1
cols = ('Usia',)
df = pd.DataFrame(np.random.radint(1,99,size=(n_rows, n_cols)),
                  columns=cols)
df

df['Kelompok_usia'] = pd.cut(df['usia'],
                             bins=[0,18,65,99],
                             labels=['anak', 'dewasa', 'manula'])
df

#14Menggunakan merge dua data frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')
df=pd.DataFrame(np.random.randint(1,20,size=(n_cols)),
                columns=cols)
df.head()

df1=df.copy(deep=True)
df1= df.drop([1,4])
df1

df2=df.copy(deep=True)
df2=df2.drop([0,3])
df2

# Menggabungkan dua data frame
df_inner = pd.merge(df1, df2, how='inner')
df_inner

df_outer= pd.merge(df1,df2, how='outer')
df_outer

#15 Memecahkan nilai string dari suatu kolom ke dalam beberapa kolom baru
data= {'nama': ['Didi kempot', 'Glen Fredly', 'Mbah surip'],
       'tempat kelahiran': ['Surakarta', 'Jawa tengah', 'Jakarta', 'DKI jakarta', 'Mojokerto']}
df = pd.DataFrame(data)
df

#Memecah nama depan dan nama belakang
df[['nama_depan', 'nama_belakang']] = df['nama'].str.split(' ', expand=True)
df

#Memecah nama Kota dan propinsi
df[['Kota', 'Propinsi']] = df['Tempat_kelahiran'].str.split(',', expand=True)
df

#16 Menata ulang data frame dengan multiple indexes menggunakan unstack()
df = pd.read_csvl('./data/titanicfull.csv')
df.head()

#Data Frame dengan multiple indexes dari hasil groupping
df.groupby(['sex', 'pclass'])['survived'].mean().to_frame()
df.groupby(['sex', 'pclass'])['survived'].mean()

#Menata ulang data frame dengan multiple indexes
df.groupby(['sex', 'pclass'])['survived'].mean().unstack()