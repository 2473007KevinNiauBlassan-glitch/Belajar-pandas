#01 Menyertakan Prefix dan suffix pada seluruh kolom data frame
import pandas as pd 
import numpy as np

print(pd.__version__)
print(np.__version__)

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                  columns=cols)
df

tuple('ABCDE')

#Menyertakan prefix kolom
df.add_prefix('kolom_')

#Menyertakan suffix kolom
df.add_suffix('_field')


#02 Pemilihan baris pada data frame
import pandas as pd 
import numpy as np

print(pd.__version__)
print(np.__version__) 

n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 5, size=(n_rows, n_cols)),
                  columns=cols)
df

#Selection dengan operator logika |
df[(df['A'] == 1) | (df['A'] == 3)]

#Selection dengan fungsi isin() dan operator negasi ~
df[df['A'].isin([1, 3])]
df[~df['A'].isin([1, 3])]


#03 Konversi tipe data string ke Numerik pada kolom data frame
import pandas as pd 

print(pd.__version__)

data = {'col1':['1', '2', '3', 'teks'],
        'col2':['1', '2', '3', '4']}

df = pd.DataFrame(data)
df

df.dtypes

#Konversi tipe data dengan fungsi astype()
df_x = df.astype({'col2':'int'})
df_x

df_x.dtypes

#Konversi tipe data numerik dengan fungsi to_numeric()
df.apply(pd.to_numeric, errors='coerce')


#04 Pemilihan kolom pada data frame berdasarkan tipe data
import pandas as pd 
import numpy as np

print(pd.__version__)
print(np.__version__)

n_rows = 5
n_cols = 2
cols = ['bil pecahan', 'bil bulat']

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)),
                  columns=cols)
df['bil pecahan'] = df['bil pecahan'].astype('float')

df.index = pd.util.testing.makeDateIndex(n_rows, freq='H')
df = df.reset_index()

df['teks'] = list('ABCDE')

df

df.dtypes

#Memilih kolom bertipe data numerik
df.select_dtypes(include='number')
df.select_dtypes(include='float')
df.select_dtypes(include='int')

#Memilih kolom bertipe data string atau object
df.select_dtypes(include='object')

#Memilih kolom bertipe data datetime
df.select_dtypes(include='datetime')

#Memilih kolom dengan kombinasi tipe data
df.select_dtypes(include=['number', 'object'])