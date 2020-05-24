import numpy as np
import pandas as pd
# read_csv
culture_center = pd.read_csv('./data/seoul_culture.csv', encoding='euc-kr')

# 필요한 열만 추출하여 저장
culture_center = culture_center[['새주소', '지번주소',
                                 '좌표정보', '좌표정보.1', '콘텐츠 명', '구명', '상세정보 값 1']]
# 결측값 제거
culture_center = culture_center.dropna()

culture_center.to_csv("df_culture_center.csv", encoding='euc-kr')
