# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

unique_values = data['whoAmI'].unique()
indices = {value: i for i, value in enumerate(unique_values)}

one_hot_data = pd.DataFrame(columns=unique_values)

for index, row in data.iterrows():
    one_hot_row = [0] * len(unique_values)
    one_hot_row[indices[row['whoAmI']]] = 1
    one_hot_data.loc[index] = one_hot_row

print(one_hot_data.head())