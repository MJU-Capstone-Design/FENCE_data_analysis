# 근린시설과 치안안전등급 간의 상관관계 분석📉

### 👤contributor

* [서유림](https://github.com/yurim22)
* [황희주](https://github.com/heejuHwang)

### 근린시설의 정의

> 「건축법」에 의한 건축물의 용도 중의 하나로 슈퍼마켓 등 보통 일상생활에 필요한 시설이며, 제 1종 근린생활시설과 제 2종 근린생활시설로 구분

* 근린시설 종류
   - 우체국
   - 병원
   - 음식점
   - 보건소
   - 은행
   - 문화시설
   - 동사무소
   - 공원
   등등....
   
🌀 근린시설의 종류들 중에서 `일반음식점` `휴게음식점` `문화시설` `공원`의 데이터를 수집해 분석에 활용하기로 결정


## 데이터

👤유림 - `휴게음식점` `문화시설` 데이터 수집 및 전처리

### 데이터 수집


**1. 휴게음식점**

* 출처 : 서울열린데이터광장
    - [데이터링크](https://data.seoul.go.kr/dataList/OA-2347/S/1/datasetView.do)
* 위의 링크는 서대문구 휴게음식점 관련 데이터

* 이와 같이 각 구별 휴게음식점 데이터를 제공해주고 있어, 25개 구의 휴게음식점에 해당하는 데이터를 다운받아 전처리 진행

* 위도 / 경도 데이터가 없어 추가해야함

**2. 문화시설**

* 출처 : 서울열린데이터광장
   - [데이터링크](https://data.seoul.go.kr/dataList/OA-13590/S/1/datasetView.do)
   
* 서울시 전체 문화시설 데이터 제공

* 주소 / 위도 / 경도 데이터 포함



### 데이터 전처리

**1. 휴게음식점**

* 폐업한 음식점까지 데이터에 포함되어 있어 폐업한 음식점 데이터는 삭제

* 필요한 열만 뽑아서 저장

* 주소를 바탕으로 위도/경도로 변환시켜 데이터 추가

* 구별로 데이터 전처리를 진행하였는데, 이후 하나의 csv 파일로 합침

   - [관련코드](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/blob/master/yurim/03corr_neigh/data_preprocessing/code/union_df.py)
   
**2. 문화시설**

* 주소데이터가 비어있는 경우가 있어, 구글맵에서 찾아 주소 및 위도/경도 데이터 추가


## 상관관계 분석📊

`근린시설`과 치안등급 간의 상관관계를 분석하는 것이므로 휴게음식점, 일반음식점, 문화시설, 공원 데이터를 하나의 요인으로 보아야 함

* 범죄율 상위 8개구와 하위 6개 구에 대해서 분석 진행

* 각 파출소 및 지구대의 관할구역 데이터를 활용하여 각 구역 별 근린시설의 수를 count

   - 파출소 및 지구대 관할구역 데이터 => [데이터](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/yurim/02secure_data)
   
   - dictionary 형태로 만들어 관할구역의 근린시설 수를 나타냄

* 각 구역별 근린시설 수와 치안등급 간의 상관분석 진행

```python 
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
```

## 분석결과


** 1. 범죄율 상위 8개 구**



<img src = "https://user-images.githubusercontent.com/33304898/82792326-30e27d80-9eaa-11ea-84f6-d29c4bfeb5a9.png" width="600" height="300">

 * 절도, 폭력에서 약한 음의 상관관계를 보임
 
 * 하지만... 너무 약해서 문제
