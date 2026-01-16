
#@author : Kevin Niau 2473007

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#29 Melakukan random sampling pada Data Frame
d={'col_1':[1,2,3,4,5],
    'col_2':[10,20,30,40,50]}
df=pd.DataFrame(d)
df

df.sample(n=4, replace=False, random_state=0)
df.sample(n=4, replace=True, random_state=0)

#30: Akses nilai variable pada query()
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')
df=pd.DataFrame(np.random.rand(1,20, size=(n_rows, n_cols)),
                columns=cols)
df

df.query('A>5')
rerata=df['A'].mean()
rerata
df.query('A>grerata')

#31 Tipe data ordinal pada Pandas Data Frame
d={'pelanggan':[11,12,13,14],
   'kepuasan':['baik', 'cukup', 'buruk', 'cukup']}
df=pd.DataFrame(d)
df

#Tipe data ordinal pada Pandas
from pandas.api.types import CategoricalDtype
kepuasan=CategoricalDtype(['buruk', 'cukup', 'baik', 'Sangat baik'],
                         ordered=True)
df['kepuasan']=df['kepuasan'].astype(tingkat_kepuasan)
df

df=df.sort_values('kepuasan', ascending=True)
df

df[df['kepuasan']>'cukup']

#33 plotting pada pandas data frame
n_rows=40
n_cols=5
cols= tuple('ABCDE')
df=pd.DataFrame(np.random.randint(1,20, size=(n_rows, n_cols)),
                columns=cols)
df.head()

df.plot(kind='line')
df[['A', 'B']].plot(kind='line')

#Bar Plot
df.head()
df.plot(kind='bar')
df[['A', 'B']].plot(kind='bar')
df[['A', 'B']].head.plot(kind='bar')
df[['A', 'B']].head.plot(kind='barh')

#Area Plot
df.head()
df.plot(kind='area')
df[['A', 'B']].head().plot(kind='area')

#Box Plot
df.head()
df.plot(kind='box')

#Histogram
df.head()
df.plot(kind='hist')
df[['A', 'B']].plot(kind='hist')

#Kernel density estimation (KDE)
df.head()
df.plot(kind='kde')

#Scatter Plot
df.head()
df.plot(x='A', y='B', kind='scatter')
