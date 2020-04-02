import pandas as pd
list1 = ['India', 'New Delhi',
         'USA', 'Washington DC',
        'Australia', 'Canberra',
        'China', 'Beijing',
        'Russia', 'Moscow']

df = pd.DataFrame()

df['Country'] = list1[0::2]
df['Capitol'] = list1[1::2]

df.to_excel('result.xls', index = False)