import csv
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import seaborn as sns    

def read_data():
    cctv = pd.read_csv('./cctv.csv')
    # rate = pd.read_csv('./secure7.csv')
    rate = pd.read_csv('./low_secure.csv')

    return cctv, rate

def make_dict(rate):
    # 각 지구대, 피출소 별 관할 구역
    boundary_dict = dict()
    for idx in range(len(rate)):
        boundary_dict[rate.loc[idx]['지구대']] = rate.loc[idx]['관할구역'].split(', ')
    # print(boundary_dict)
   
    # 각 지구대, 파출소 별 치안 등급 (전체, 살인, 강도, 절도, 폭력, 성폭력)
    rate_dict = dict()
    col_list = list(rate)[:6] # 컬럼명
    for idx in range(len(rate)):
        rate_dict[rate.loc[idx]['지구대']] = dict()
        for c in col_list:
            rate_dict[rate.loc[idx]['지구대']][c] = rate.loc[idx][c]
    # print(rate_dict)

    # 각 지구대, 파출소 별 cctv 갯수 초기화
    cctv_num = dict()
    for idx in range(len(rate)):
        cctv_num[rate.loc[idx]['지구대']] = 0

    return boundary_dict, rate_dict, cctv_num

# 각 지구대별 cctv개수 세기
def count_cctv(boundary_dict, cctv_num, rate):
    keys = boundary_dict.keys()
    no_cnt = 0
    for key in keys:
        boundaries = boundary_dict[key]
        for idx in range(len(cctv)):
            street = str(cctv.loc[idx]['도로명주소'])
            addr = str(cctv.loc[idx]['지번주소'])
            for bd in boundaries:
                if bd in addr:
                    cctv_num[key] += int(cctv.loc[idx]['카메라대수'])
                    continue
                elif bd in street:
                    cctv_num[key] += int(cctv.loc[idx]['카메라대수'])
                    continue
        cctv_num[key]
        print(key)
    print(cctv_num)
    return cctv_num

# 상관분석
def correlation(cctv_num, rate):
    cctv_df = pd.DataFrame(cctv_num.items(), columns=['지구대', 'cctv'])
    merge_rate_cctv = pd.merge(cctv_df, rate, on='지구대')
    print(merge_rate_cctv)
    corr_df = merge_rate_cctv[['전체','살인','강도','절도','폭력','성폭력','cctv']]
    rate_cctv_ad = merge_rate_cctv[['전체','살인','강도','절도','폭력','성폭력','cctv', '구']]
    # print('corr_df :', corr_df)
    print('sum: ', corr_df['cctv'].sum())
    corr_df.to_csv("./corr_d.csv", header=True, index=False)
    rate_cctv_ad.to_csv("./rate_cctv_ad.csv", header=True, index=False)

    corr = corr_df.corr(method= 'pearson')
    print('corr :', corr)
    corr.to_csv("./corr.csv", header=True, index=False)
    return

# 각 구별 상관분석 
def corr_ad():
    ad = ['종로구', '중구', '마포구', '영등포구']
    corr_df = pd.read_csv('./rate_cctv_ad.csv')

    for i in range(len(ad)):
        is_ad = corr_df[corr_df['구'] == ad[i]]
        # print(is_ad)
        corr = is_ad.corr(method= 'pearson')
        print(ad[i],':', corr)
    return

cctv, rate = read_data()
boundary_dict, rate_dict, cctv_num = make_dict(rate)
cctv_num = count_cctv(boundary_dict, cctv_num, cctv)
correlation(cctv_num, rate)
# corr_ad()


