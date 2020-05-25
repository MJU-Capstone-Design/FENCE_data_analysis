import csv
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import seaborn as sns    

def read_data():
    light = pd.read_csv('./light.csv')
    rate = pd.read_csv('./secure7.csv')

    return light, rate

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

    # 각 지구대, 파출소 별 light 갯수 초기화
    light_num = dict()
    for idx in range(len(rate)):
        light_num[rate.loc[idx]['지구대']] = 0

    return boundary_dict, rate_dict, light_num

# 각 지구대별 light개수 세기
def count_light(boundary_dict, light_num, rate):
    keys = boundary_dict.keys()
    no_cnt = 0
    for key in keys:
        boundaries = boundary_dict[key]

        for idx in range(len(light)):
            street = str(light.loc[idx]['소재지도로명주소'])
            addr = str(light.loc[idx]['소재지지번주소'])
            for bd in boundaries:
                if bd in addr:
                    light_num[key] += int(light.loc[idx]['설치개수'])
                    continue
                elif bd in street:
                    light_num[key] += int(light.loc[idx]['설치개수'])
                    continue
        light_num[key]
        print(key)
    # print(light_num)
    return light_num

# 상관분석
def correlation(light_num, rate):
    light_df = pd.DataFrame(light_num.items(), columns=['지구대', 'light'])
    merge_rate_light = pd.merge(light_df, rate, on='지구대')
    merge_rate_light.to_csv("./merge_rate_light.csv", header=True, index=False, encoding='utf-8')
    # print(merge_rate_light)

    corr_df = merge_rate_light[['전체','살인','강도','절도','폭력','성폭력','light']]
    rate_light_ad = merge_rate_light[['전체','살인','강도','절도','폭력','성폭력','light', '구']]
    print('sum: ', corr_df['light'].sum())
    # corr_df.to_csv("./corr_d.csv", header=True, index=False)
    rate_light_ad.to_csv("./rate_light_ad.csv", header=True, index=False)

    corr = corr_df.corr(method= 'pearson')
    print('corr :', corr)
    corr.to_csv("./corr.csv", header=True, index=False)
    return

# 각 구별 상관분석 
def corr_ad():
    ad = ['종로구', '중구', '마포구', '영등포구']
    corr_df = pd.read_csv('./rate_light_ad.csv')

    for i in range(len(ad)):
        is_ad = corr_df[corr_df['구'] == ad[i]]
        # print(is_ad)
        corr = is_ad.corr(method= 'pearson')
        print(ad[i],':', corr)
    return

light, rate = read_data()
boundary_dict, rate_dict, light_num = make_dict(rate)
light_num = count_light(boundary_dict, light_num, light)
correlation(light_num, rate)
# corr_ad()


