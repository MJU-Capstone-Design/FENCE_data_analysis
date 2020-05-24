import numpy as np
import pandas as pd

# read_csv
junggu = pd.read_csv('res_junggu.csv', encoding='euc-kr')
# 필요한 열만 추출하여 저장
df_junggu = junggu[['업종명', '업소명', '소재지도로명',
                    '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
# 폐업되지 않은 가게만을 추출
df_junggu[df_junggu['폐업구분'].isnull()]
df_junggu = df_junggu[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]

jungrang = pd.read_csv('res_jungrang.csv', encoding='euc-kr')
df_jungrang = jungrang[['업종명', '업소명', '소재지도로명',
                        '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_jungrang[df_jungrang['폐업구분'].isnull()]
df_jungrang = df_jungrang[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_jungrang

mapo = pd.read_csv('res_mapo.csv', encoding='euc-kr')
df_mapo = mapo[['업종명', '업소명', '소재지도로명',
                '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_mapo[df_mapo['폐업구분'].isnull()]
df_mapo = df_mapo[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_mapo

dobong = pd.read_csv('res_dobong.csv', encoding='euc-kr')
df_dobong = dobong[['업종명', '업소명', '소재지도로명',
                    '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_dobong[df_dobong['폐업구분'].isnull()]
df_dobong = df_dobong[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_dobong

dongdaemoon = pd.read_csv('res_dongdaemoon.csv', encoding='euc-kr')
df_dongdaemoon = dongdaemoon[['업종명', '업소명',
                              '소재지도로명', '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_dongdaemoon[df_dongdaemoon['폐업구분'].isnull()]
df_dongdaemoon = df_dongdaemoon[[
    '업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_dongdaemoon

dongjak = pd.read_csv('res_dongjak.csv', encoding='euc-kr')
df_dongjak = dongjak[['업종명', '업소명', '소재지도로명',
                      '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_dongjak[df_dongjak['폐업구분'].isnull()]
df_dongjak = df_dongjak[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_dongjak

eunpeung = pd.read_csv('res_eunpeung.csv', encoding='euc-kr')
df_eunpeung = eunpeung[['업종명', '업소명', '소재지도로명',
                        '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_eunpeung[df_eunpeung['폐업구분'].isnull()]
df_eunpeung = df_eunpeung[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_eunpeung

gangbook = pd.read_csv('res_gangbook.csv', encoding='euc-kr')
df_gangbook = gangbook[['업종명', '업소명', '소재지도로명',
                        '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_gangbook[df_gangbook['폐업구분'].isnull()]
df_gangbook = df_gangbook[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_gangbook

gangnam = pd.read_csv('res_gangnam.csv', encoding='euc-kr')
df_gangnam = gangnam[['업종명', '업소명', '소재지도로명',
                      '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_gangnam[df_gangnam['폐업구분'].isnull()]
df_gangnam = df_gangnam[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_gangnam

gangseo = pd.read_csv('res_gangseo.csv', encoding='euc-kr')
df_gangseo = gangseo[['업종명', '업소명', '소재지도로명',
                      '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_gangseo[df_gangseo['폐업구분'].isnull()]
df_gangseo = df_gangseo[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_gangseo

geumcheon = pd.read_csv('res_geumcheon.csv', encoding='euc-kr')
df_geumcheon = geumcheon[['업종명', '업소명', '소재지도로명',
                          '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_geumcheon[df_geumcheon['폐업구분'].isnull()]
df_geumcheon = df_geumcheon[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_geumcheon

guro = pd.read_csv('res_guro.csv', encoding='euc-kr')
df_guro = guro[['업종명', '업소명', '소재지도로명',
                '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_guro[df_guro['폐업구분'].isnull()]
df_guro = df_guro[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_guro

gwanak = pd.read_csv('res_guro.csv', encoding='euc-kr')
df_gwanak = gwanak[['업종명', '업소명', '소재지도로명',
                    '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_gwanak[df_gwanak['폐업구분'].isnull()]
df_gwanak = df_gwanak[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_gwanak

gwangjin = pd.read_csv('res_gwangjin.csv', encoding='euc-kr')
df_gwangjin = gwangjin[['업종명', '업소명', '소재지도로명',
                        '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_gwangjin[df_gwangjin['폐업구분'].isnull()]
df_gwangjin = df_gwangjin[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_gwangjin

jongro = pd.read_csv('res_jongro.csv', encoding='euc-kr')
df_jongro = jongro[['업종명', '업소명', '소재지도로명',
                    '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_jongro[df_jongro['폐업구분'].isnull()]
df_jongro = df_jongro[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_jongro

nowon = pd.read_csv('res_nowon.csv', encoding='euc-kr')
df_nowon = nowon[['업종명', '업소명', '소재지도로명',
                  '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_nowon[df_nowon['폐업구분'].isnull()]
df_nowon = df_nowon[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_nowon

seocho = pd.read_csv('res_seocho.csv', encoding='euc-kr')
df_seocho = seocho[['업종명', '업소명', '소재지도로명',
                    '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_seocho[df_seocho['폐업구분'].isnull()]
df_seocho = df_seocho[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_seocho

seodaemoon = pd.read_csv('res_seodaemoon.csv', encoding='euc-kr')
df_seodaemoon = seodaemoon[['업종명', '업소명', '소재지도로명',
                            '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_seodaemoon[df_seodaemoon['폐업구분'].isnull()]
df_seodaemoon = df_seodaemoon[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_seodaemoon

songpa = pd.read_csv('res_songpa.csv', encoding='euc-kr')
df_songpa = songpa[['업종명', '업소명', '소재지도로명',
                    '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_songpa[df_songpa['폐업구분'].isnull()]
df_songpa = df_songpa[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_songpa

sungbuk = pd.read_csv('res_sungbuk.csv', encoding='euc-kr')
df_sungbuk = sungbuk[['업종명', '업소명', '소재지도로명',
                      '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_sungbuk[df_sungbuk['폐업구분'].isnull()]
df_sungbuk = df_sungbuk[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_sungbuk

youngsan = pd.read_csv('res_youngsan.csv', encoding='euc-kr')
df_youngsan = youngsan[['업종명', '업소명', '소재지도로명',
                        '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_youngsan[df_youngsan['폐업구분'].isnull()]
df_youngsan = df_youngsan[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_youngsan

sungdong = pd.read_csv('res_sungdong.csv', encoding='euc-kr')
df_sungdong = sungdong[['업종명', '업소명', '소재지도로명',
                        '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_sungdong[df_sungdong['폐업구분'].isnull()]
df_sungdong = df_sungdong[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_sungdong

df_youngdeungpo = youngdeungpo[[
    '업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_youngdeungpo[df_youngdeungpo['폐업구분'].isnull()]
df_youngdeungpo = df_youngdeungpo[[
    '업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_youngdeungpo

yangcheon = pd.read_csv('res_yangcheon.csv')

df_yangcheon = yangcheon[['업종명', '업소명', '소재지도로명',
                          '소재지지번', '행정동명', '폐업일자', '폐업구분', '업태명']]
df_yangcheon[df_yangcheon['폐업구분'].isnull()]
df_yangcheon = df_yangcheon[['업종명', '업소명', '소재지도로명', '소재지지번', '행정동명', '업태명']]
df_yangcheon
df_yangcheon.to_csv("df_resyangcheon.csv", encoding='euc-kr')

# 완성된 데이터 프레임을 csv파일 형식으로 저장
df_junggu.to_csv("df_resjunggu.csv", encoding='euc-kr')
df_jungrang.to_csv("df_resjungrang.csv", encoding='euc-kr')
df_mapo.to_csv("df_resmapo.csv", encoding='euc-kr')
df_youngdeungpo.to_csv("df_resyoungdeungpo.csv", encoding='euc-kr')
df_sungdong.to_csv("df_ressungdong.csv", encoding='euc-kr')
df_dobong.to_csv("df_resdobong.csv", encoding='euc-kr')
df_dongdaemoon.to_csv("df_resdongdaemoon.csv", encoding='euc-kr')
df_dongjak.to_csv("df_resdongjak.csv", encoding='euc-kr')
df_eunpeung.to_csv("df_reseunpeung.csv", encoding='euc-kr')

df_gangbook.to_csv("df_resgangbook.csv", encoding='euc-kr')
df_gangseo.to_csv("df_resgangseo.csv", encoding='euc-kr')
df_gangnam.to_csv("df_resgangnam.csv", encoding='euc-kr')
# df_gang.to_csv("df_resgang.csv", encoding='euc-kr')

df_geumcheon.to_csv("df_resgeumcheon.csv", encoding='euc-kr')
df_guro.to_csv("df_resguro.csv", encoding='euc-kr')
df_gwanak.to_csv("df_resgwanak.csv", encoding='euc-kr')
df_gwangjin.to_csv("df_resgwangjin.csv", encoding='euc-kr')

df_jongro.to_csv("df_resjongro.csv", encoding='euc-kr')
df_nowon.to_csv("df_resnowon.csv", encoding='euc-kr')
df_seocho.to_csv("df_resseocho.csv", encoding='euc-kr')
df_seodaemoon.to_csv("df_resseodaemoon.csv", encoding='euc-kr')

df_songpa.to_csv("df_ressongpa.csv", encoding='euc-kr')
df_sungbuk.to_csv("df_ressungbuk.csv", encoding='euc-kr')
df_youngsan.to_csv("df_resyoungsan.csv", encoding='euc-kr')
