import csv
import pandas as pd
import scipy.stats as stats

def read_data():
    rate = pd.read_csv('./secure2.csv')
    return rate

goo = ['중구', '종로구', '마포구', '영등포구', '용산구', '금천구', '강남구', '구로']
police_rank_mean = {'중구':2.93, '종로구':3.3, '마포구':3.25, '영등포구':3.6, '용산구':3.71, '금천구':3, '강남구':3.36, '구로':3}

police_s_mean = {'중구':1.4, '종로구':1.8, '마포구':2.15, '영등포구':3.8, '용산구':1.86, '금천구':1.6, '강남구':2.21, '구로':3}
police_k_mean = {'중구':2.13, '종로구':2.1, '마포구':2.625, '영등포구':3.2, '용산구':3.14, '금천구':2.4, '강남구':3, '구로':2.625}
police_j_mean = {'중구':3.07, '종로구':3.05, '마포구':2.375, '영등포구':3.3, '용산구':2.86, '금천구':1.6, '강남구':2.64, '구로':2.75}
police_p_mean = {'중구':2.4, '종로구':3.25, '마포구':2.625, '영등포구':3.6, '용산구':2.71, '금천구':2, '강남구':2, '구로':3}
police_sp_mean = {'중구':3.2, '종로구':3.15, '마포구':3.625, '영등포구':3.7, '용산구':3.86, '금천구':2.8, '강남구':3.36, '구로':3.25}

police_num = {'중구':12, '종로구':15, '마포구':18, '영등포구':16, '용산구':13, '금천구':13, '강남구':12, '구로':18}

p_df = pd.DataFrame(police_num.items(), columns=['구', '경찰서수'])
p_r_m_df = pd.DataFrame(police_rank_mean.items(), columns=['구', '평균 등급'])
merge_df = pd.merge(p_df, p_r_m_df, on='구')
corr_df = merge_df[['경찰서수','평균 등급']]
corr = corr_df.corr(method= 'pearson')
print('전체 등급 평균')
print(corr)

p_r_m_df = pd.DataFrame(police_s_mean.items(), columns=['구', '평균 등급'])
merge_df = pd.merge(p_df, p_r_m_df, on='구')
corr_df = merge_df[['경찰서수','평균 등급']]
corr = corr_df.corr(method= 'pearson')
print('살인 등급 평균')
print(corr)

p_r_m_df = pd.DataFrame(police_k_mean.items(), columns=['구', '평균 등급'])
merge_df = pd.merge(p_df, p_r_m_df, on='구')
corr_df = merge_df[['경찰서수','평균 등급']]
corr = corr_df.corr(method= 'pearson')
print('강도 등급 평균')
print(corr)

p_r_m_df = pd.DataFrame(police_j_mean.items(), columns=['구', '평균 등급'])
merge_df = pd.merge(p_df, p_r_m_df, on='구')
corr_df = merge_df[['경찰서수','평균 등급']]
corr = corr_df.corr(method= 'pearson')
print('절도 등급 평균')
print(corr)

p_r_m_df = pd.DataFrame(police_p_mean.items(), columns=['구', '평균 등급'])
merge_df = pd.merge(p_df, p_r_m_df, on='구')
corr_df = merge_df[['경찰서수','평균 등급']]
corr = corr_df.corr(method= 'pearson')
print('폭력 등급 평균')
print(corr)

p_r_m_df = pd.DataFrame(police_sp_mean.items(), columns=['구', '평균 등급'])
merge_df = pd.merge(p_df, p_r_m_df, on='구')
corr_df = merge_df[['경찰서수','평균 등급']]
corr = corr_df.corr(method= 'pearson')
print('성폭력 등급 평균')
print(corr)

