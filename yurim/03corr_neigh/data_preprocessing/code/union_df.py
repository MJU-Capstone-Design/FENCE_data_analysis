import pandas as pd

mapo_res = pd.read_csv('./data/df_resmapo.csv', encoding='euc-kr')
junggu_res = pd.read_csv('./data/df_resjunggu.csv', encoding='euc-kr')
jongro_res = pd.read_csv('./data/df_resjongro.csv', encoding='euc-kr')
youngdeungpo_res = pd.read_csv(
    './data/df_resyoungdeungpo.csv', encoding='euc-kr')

# 범죄율 top4 자치구 휴게음식점 데이터 합치기
rest_restaurant = pd.concat(
    [mapo_res, junggu_res, jongro_res, youngdeungpo_res])

rest_restaurant.to_csv("rest_restaurant.csv", encoding='euc-kr')

# 범죄율 top5~8 휴게음식점 데이터 합치기
youngsan_res = pd.read_csv('./data/df_resyoungsan.csv', encoding='euc-kr')
gangnam_res = pd.read_csv('./data/df_resgangnam.csv', encoding='euc-kr')
geumcheon_res = pd.read_csv('./data/df_resgeumcheon.csv', encoding='euc-kr')
guro_res = pd.read_csv('./data/df_resguro.csv', encoding='euc-kr')

rest_restaurant2 = pd.concat(
    [youngsan_res, gangnam_res, geumcheon_res, guro_res])

rest_restaurant2.to_csv("rest_restaurant2.csv", encoding='euc-kr')

# 범죄율 top1~8 휴게음식점 데이터 합치기
rest_pre = pd.read_csv('./data/df_rest_restaurant.csv', encoding='euc-kr')
rest_post = pd.read_csv('./data/rest_restaurant2.csv', encoding='euc-kr')

rest_restaurant_fin = pd.concat([rest_pre, rest_post])

rest_restaurant_fin.to_csv("df_rest_restaurant2.csv", encoding='euc-kr')

# 범죄율 하위 6개 구 휴게음식점 데이터

gangseo_res = pd.read_csv('./data/df_resgangseo.csv', encoding='euc-kr')
yangcheon_res = pd.read_csv('./data/df_resyangcheon.csv', encoding='euc-kr')
nowon_res = pd.read_csv('./data/df_resnowon.csv', encoding='euc-kr')
sungbuk_res = pd.read_csv('./data/df_ressungbuk.csv', encoding='euc-kr')
dobong_res = pd.read_csv('./data/df_resdobong.csv', encoding='euc-kr')
eunpeung_res = pd.read_csv('./data/df_reseunpeung.csv', encoding='euc-kr')

rest_restaurant3 = pd.concat(
    [gangseo_res, yangcheon_res, nowon_res, sungbuk_res, dobong_res, eunpeung_res])

rest_restaurant3.to_csv("rest_restaurant3.csv", encoding='euc-kr')
