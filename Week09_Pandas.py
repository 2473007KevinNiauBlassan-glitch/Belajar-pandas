#@author : Kevin Niau 2473007

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#33 Menampilkan nilai kumulatif 
d={'pemain':['Budi','Joni','Iwan','Budi','Iwan','Asep', 'Joni'],
    'goal':[2,1,3,1,1,2,2,3]}
df=pd.DataFrame(d)
df

df['goal'].consum().to_frame()
df['jumlah_goal_kumulatif'] = df['goal'].cumsum()
df['jumlah_goal_kumulatif_tiap_pemain'] = df.groupby('pemain')['goal'].cumsum()
df['cummax'] = df['goal'].cummax()
df['cummin'] = df['goal'].cummin()
df['cumprod'] = df['goal'].cumprod()

#34 Mapping pada Data Frame dengan applymap()
df=pd.DataFrame({'Jenis_klamin':['Pria','Wanita', 'lelaki','perempuan'],
                'usia':[23,21,24,22,21],
                'shift':['pagi','siang','malam','siang','pagi']})

df.df.applymap(lambda x:x.lower()) if type(x)==str else x
df

#applymap() dengan dictionary
mapping={'pria':'L',
         'lelaki':'L',
         'wanita':'P',
         'perempuan':'P',
         'pagi':1,
         'siang':2,
         'malam':3}
df.applymap(mapping.get)

df[['Jenis_klamin', 'shift']] = df[['Jenis_klamin', 'shift']].applymap(mapping.get)
df

#35 Memadukan fungsi agregasi dengan transform()
d={'no_nota':[1,1,1,2,2,3,4,5],
   'kopi':['latte', 'cappucino', 'latte', 'espresso', 'cappuccino', 'latte', 'espresso'],
   'harga':[50, 60, 80, 150, 120, 60, 100, 40]}
df=pd.DataFrame(d)
df

#Menghitung total harga untuk nomor nota
df.groupby('no_nota')['harga'].sum().to_frame()
df['total_harga'] = df.groupby('no_nota')['harga'].transform('sum')
df

#Menghitung total omset untuk tiap jenis kopi yang terjual
df.groupby('kopi')['harga'].sum().to_frame()
df['total_omset'] = df.groupby('kopi')['harga'].transform('sum')
df

#36 Menyatukan kolom dengan str.cat()
data={'nama':['Bayu', 'indra', 'devi', 'agni'],
      'Jenis_kelamin':['L', 'L', 'P', 'L'],
      'usia':[23, 21, 22, 25]}
df=pd.DataFrame(data)
df

#Menyatukan kolom dengan str.cat()
df['nama'].str.cat(df['Jenis_kelamin'], sep=',').to_frame()
df['nama_jk']=df['nama'].str.cat(df['Jenis_kelamin'], sep=',')
df
df['nama'].str.cat(df['usia'].astype(str), sep='-').to_frame()
df['nama_usia']=df['nama'].str.cat(df['usia'].astype(str), sep='-').to_frame()
df