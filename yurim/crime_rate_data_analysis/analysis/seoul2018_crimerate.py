import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib as mlp

data = pd.read_csv('../data/crimes2018.csv', encoding='euc-kr')

idx_arrest = data[data['발생검거'] == '검거'].index
data_occur = data.drop(idx_arrest)

grouped_data = data_occur.groupby(by=['구분'], as_index=False).sum()

grouped_data.iloc[8, 0] = '중구'
grouped_data.iloc[14, 0] = '서초구'
grouped_data.iloc[16, 0] = '마포구'
grouped_data.iloc[21, 0] = '강남구'
grouped_data.iloc[27, 0] = '성북구'
grouped_data.iloc[30, 0] = '종로구'

grouped2_data = grouped_data.groupby(by=['구분'], as_index=False).sum()
grouped2_data.shape

population = pd.read_csv('../data/population_seoul2018.csv', encoding='euc-kr')
population = population.iloc[1:, :]
population['총인구수'] = pd.to_numeric(population['총인구수'])

join_data = pd.merge(grouped2_data, population, left_on='구분',
                     right_on='행정구역(시군구)별', how='outer')
crime_rate = (join_data['건수'] / join_data['총인구수']) * 100000

join_data['crime_rate'] = crime_rate
join_data.sort_values(by=['crime_rate'], ascending=False)

crime_data = join_data[['행정구역(시군구)별', 'crime_rate']]
crime_rate_sorted = crime_data.sort_values(by=['crime_rate'], ascending=False)

crime_rate_sorted.to_csv("seoul_crime_rate.csv", encoding='euc-kr')
