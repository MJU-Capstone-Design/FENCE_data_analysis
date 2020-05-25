import csv
import pandas as pd
import scipy.stats as stats

# 범죄율 상위 8개 구 상관관계 분석


def read_data():
    culture_center = pd.read_csv(
        './data/df_culture_center.csv', encoding='euc-kr', dtype={"새주소": str, "지번주소": str, "X": float, "Y": float, "콘텐츠 명": str, "구명": str, "상세정보 값1": str})
    rest_restaurant = pd.read_csv(
        './data/df_rest_restaurant2.csv', encoding='euc-kr')
    restaurant = pd.read_csv(
        './data/df_seoul_restaurant2.csv', encoding='euc-kr')
    park = pd.read_csv('./data/df_seoul_park.csv', encoding='euc-kr')
    rate = pd.read_csv('./data/secure_7_rm.csv', dtype={'전체': int, '살인': int, '강도': int, '절도': int,
                                                        '폭력': int, '성폭력': int, '구' '주소': str, '위도': float, '경도': float, '지구대': str, '관할구역': str})

    rate = rate.dropna()
    return culture_center, rest_restaurant, restaurant, park, rate


def make_dict(rate):
    # 각 지구대, 피출소 별 관할 구역
    boundary_dict = dict()
    # str(rate['관할구역'])
    for idx in range(len(rate)):
        boundary_dict[rate.loc[idx]['지구대']] = rate.loc[idx]['관할구역'].split(', ')
    # print(boundary_dict)

    # 각 지구대, 파출소 별 치안 등급 (전체, 살인, 강도, 절도, 폭력, 성폭력)
    rate_dict = dict()
    col_list = list(rate)[:6]  # 컬럼명
    for idx in range(len(rate)):
        rate_dict[rate.loc[idx]['지구대']] = dict()
        for c in col_list:
            rate_dict[rate.loc[idx]['지구대']][c] = rate.loc[idx][c]
    # print(rate_dict)

    # 각 지구대, 파출소 별 근린시설 갯수 초기화
    green_num = dict()
    for idx in range(len(rate)):
        green_num[rate.loc[idx]['지구대']] = 0

    return boundary_dict, rate_dict, green_num

# 각 지구대별 근린공원개수 세기

# 문화시설


def count_culture_center(boundary_dict, green_num, rate):
    keys = boundary_dict.keys()
    no_cnt = 0
    for key in keys:
        boundaries = boundary_dict[key]
        for idx in range(len(culture_center)):
            street = str(culture_center.loc[idx]['새주소'])
            addr = str(culture_center.loc[idx]['지번주소'])
            for bd in boundaries:
                if bd in addr:
                    green_num[key] += 1
                    continue
                elif bd in street:
                    green_num[key] += 1
                    continue
        # culture_center_num[key] /= len(boundaries)
        # print(key)
    # print(green_num)
    return green_num

# 휴게음식점


def count_rest_restaurant(boundary_dict, green_num, rate):
    keys = boundary_dict.keys()
    no_cnt = 0
    for key in keys:
        boundaries = boundary_dict[key]
        for idx in range(len(rest_restaurant)):
            dong = str(rest_restaurant.loc[idx]['행정동명'])
            addr = str(rest_restaurant.loc[idx]['소재지지번'])
            for bd in boundaries:
                if bd in dong:
                    green_num[key] += 1
                    continue
                elif bd in addr:
                    green_num[key] += 1
                    continue

        # culture_center_num[key] /= len(boundaries)
        # print(key)
    # print(green_num)
    return green_num

# 일반음식점


def count_restaurant(boundary_dict, green_num, rate):
    keys = boundary_dict.keys()
    no_cnt = 0
    for key in keys:
        boundaries = boundary_dict[key]
        for idx in range(len(restaurant)):
            dong = str(restaurant.loc[idx]['행정동명'])
            addr = str(restaurant.loc[idx]['소재지지번'])
            for bd in boundaries:
                if bd in dong:
                    green_num[key] += 1
                    continue
                elif bd in addr:
                    green_num[key] += 1
                    continue
        # culture_center_num[key] /= len(boundaries)
        # print(key)
    # print(green_num)
    return green_num

# 공원


def count_park(boundary_dict, green_num, rate):
    keys = boundary_dict.keys()
    no_cnt = 0
    for key in keys:
        boundaries = boundary_dict[key]
        for idx in range(len(park)):
            dong = str(park.loc[idx]['행정동'])
            addr = str(park.loc[idx]['공원주소'])
            for bd in boundaries:
                if bd in dong:
                    green_num[key] += 1
                    continue
                elif bd in addr:
                    green_num[key] += 1
                    continue
        # culture_center_num[key] /= len(boundaries)
        # print(key)
#     print(green_num)
    return green_num


culture_center, rest_restaurant, restaurant, park, rate = read_data()

boundary_dict, rate_dict, green_num = make_dict(rate)

count_culture_center(
    boundary_dict, green_num, culture_center)
count_rest_restaurant(boundary_dict, green_num, rest_restaurant)
count_restaurant(boundary_dict, green_num, restaurant)
green_num = count_park(boundary_dict, green_num, park)

print(green_num)
# correlation(cctv_num, rate)
# corr_ad()


def correlation(green_num, rate):
    green_df = pd.DataFrame(green_num.items(), columns=['지구대', '근린시설'])
    merge_rate_green = pd.merge(green_df, rate, on='지구대')
    corr_df = merge_rate_green[['근린시설', '전체', '살인', '강도', '절도', '폭력', '성폭력']]
    # print('corr_df :', corr_df)
    print('sum: ', corr_df['근린시설'].sum())
    corr_df.to_csv("./corr_df.csv", header=True, index=False)

    corr = corr_df.corr(method='pearson')
    print('corr :', corr)
    corr.to_csv("./corr.csv", header=True, index=False)
    return corr
