import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#17 Resampling pada data deret waktu (time series data)
n_rows = 365 * 24
n_cols = 2
cols = ['col1', 'col2']
df = pd.Dataframe(np.random.radint(1,20, size=(n_rows, n_cols)),
                    columns=cols)
df.index=pd.util.testing.makeDateIndex(n_rows, ferq='H')
df

# Resampling data dengan interval monthly
df.resample('M')['col1'].sum().to_frame()

#18 Membentuk dummmy Data Frame
pd.DataFrame({'col1':[1,2,3,4],
               'Col2': [5,6,7,8]})

#Membentuk Data Frame dari Numpy array
n_rows = 5
n_cols = 3
arr = np.random.randint(1,20, size=(n_rows, n_cols))
arr
pd.DataFrame(arr, columns=tuple('ABC'))
pd.util.testing.makeDataFrame().head()
pd.util.testing.makeMixedDataFrame().head()
pd.util.testing.makeTimeDataFrame().head()
pd.util.testing.makeMissDataFrame().head()

# 19 Formating tampilan Data Frame
n_rows = 5
n_cols = 2
cols=['omset', 'operasional']
df = pd.DataFrame(np.random.radint(1,20,size=(n_rows, n_cols)),
                    columns=cols)
df

df['omset']=df['omset']*100_000
df['operasional']=df['operasional']*10_000
df

df.index=pd.util.testing.makeDateIndex(n_rows, freq='D')
df=df.reset_index()
df=df.rename(columns={'index':'tanggal'})
df

# Melakukan fortmatting tampilan Data Frame
fromatku= {'tanggal':'{:5d/%m/%y}',
           'operasional':'Rp {:.2f}',
           'omset':'Rp {:.2f}'} 

laporan = df.style.format(formatku)
laporan
type(laporan)
laporan.hide_index()
laporan.set_caption('Data Omset dan Operational')
laporan.highlight_min('omset', color='pink')
laporan.highlinght_max('omset', color='lightgreen')

laporan.highlight_min('operasional', color='lightblue')
laporan.highlight_max('operasional', color='grey')

#20 Menggabungkan (merge) dua Data frame secara berdampingan
d1 = {'col1':[1,2,3],
        'col2':[10,20,30]}
df2= pd.DataFrame(d1)
df2

d1 = {'col1':[4,5,6],
        'col2':[40,50,60]}
df2= pd.DataFrame(d2)
df2

# Menggabungkan merge dua data frame secara berdampingan
df= pd.merge(df1, df2, left_index=True, right_index=True)
df