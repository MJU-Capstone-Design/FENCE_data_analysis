# FENCE Project 데이터 분석🚧


### 데이터 전처리부터 분석까지👩‍💻


### 👤contributor

* [최리안](https://github.com/leeeeean)
* [배수혜](https://github.com/Uranel)
* [황희주](https://github.com/heejuHwang)
* [서유림](https://github.com/yurim22)

--------------------------------------------------

## Fence Project?🚧

* 2020-1학기 명지대학교 캡스톤 디자인 수업에서 진행하는 프로젝트입니다.

* 범죄예방 이론 및 정책 중에서도 CPTED의 뛰어난 범죄 예방 효과에 주목하여, 이를 기반으로 한 통계적 분석과 그 결과를 통한 안전지도의 구현을 최종 목표로 합니다.

> CPTED란?

> 'Crime Prevention Through Environmental Design'의 약자로, '환경설계를 통한 범죄예방'을 의미합니다.


### 분석문항

📎 [**분석1.** 서울특별시 각 자치구 범죄율 순위](#분석1-서울특별시-각-자치구-범죄율-순위)

📎 [**분석2.** CPTED의 5가지 물리적 요인과 치안 등급의 관계](#분석2-CPTED의-5가지-물리적-요인과-치안-등급의-관계)

📎 [**분석2-1.** cctv 수는 치안 등급에 영향을 미치는가?](#분석2-1-cctv와-치안안전등급-간의-상관관계-분석)

📎 [**분석2-2.** 보안등 수는 치안 등급에 영향을 미치는가?](#분석2-2-보안등과-치안안전등급-간의-상관관계-분석)

📎 [**분석2-3.** 경비원 수는 치안 등급에 영향을 미치는가?](#분석2-3-경비인원-수와-치안안전등급-간의-상관관계-분석)

📎 [**분석2-4.** 파출소 수는 치안 등급에 영향을 미치는가?](#분석2-4-파출소-수와-치안안전등급-간의-상관관계-분석)

📎 [**분석2-5.** 근린시설 수는 치안 등급에 영향을 미치는가?](#분석2-5-근린시설과-치안안전등급-간의-상관관계-분석)


-------------------------------------------------------------------------

## 분석1. 서울특별시 각 자치구 범죄율 순위

👤contributor : [서유림](https://github.com/yurim22)

* 서울시내 모든 자치구에 대해 범죄등급을 조사하고 분석하는 데에는 무리가 있다고 판단하여 범죄율이 높은 자치구를 선별하여 분석을 진행하고자 한다.
    - 이후 추가적으로 범죄율이 낮은 6개의 자치구에 대해서도 분석 진행
    - 범죄율 상위 8개구 / 범죄율 하위 6개구 선별
    
* 이에 모든 분석과정에 앞서 서울시 내 자치구 범죄율 순위를 분석하는 과정을 거친다.

### 📋활용한 데이터

* 서울시 관서별 5대범죄(2018년)
   - 출처 : 공공데이터 포털 
   - [홈페이지](https://www.data.go.kr/data/15054737/fileData.do)

* 서울시 인구분포(2018년)
   - 출처 : 국가통계포털 
   - [홈페이지](http://kosis.kr/index/index.do)
   
   
### ✏️분석 방법
> 범죄율=(형법범죄 / 총인구) ×  100,000

* 서울시 자치구별 발생한 5대범죄 건수를 파악하고 총 범죄 발생 건수를 구한다.
* 범죄율 구하는 공식에 따라 범죄 발생건수를 자치구 인구 수로 나누어 주고 100000을 곱한다.
* 인구 십만명 당 발생하는 범죄 건수를 구하여 sorting한다.

1. 범죄율 순위 결과(table)

![범죄율 순위표](https://user-images.githubusercontent.com/33304898/82736405-8a409480-9d64-11ea-94ef-3ebe06b204ec.JPG)

2. 범죄율 시각화(plot)

<img src="https://user-images.githubusercontent.com/33304898/82801273-05ff2600-9eb8-11ea-8faa-e6aec62b0786.png"  width="600" height="370">


### ✏️분석 결과
* 중구 / 종로구 / 마포구 / 영등포구 / 용산구 / 금천구 / 강남구 / 구로구 순으로 범죄율이 높게 나타났다.

* 은평구 / 도봉구 / 성북구 / 노원구 / 양천구 / 강서구 순으로 범죄율이 낮게 나타났다.

### 이후 활동

* 각 구별로 데이터를 수집하고 전처리를 진행한다.

----------------------------------------------------------------------------

## 분석2. CPTED의 5가지 물리적 요인과 치안 등급의 관계


👤contributor

* [최리안](https://github.com/leeeeean)
* [배수혜](https://github.com/Uranel)
* [황희주](https://github.com/heejuHwang)
* [서유림](https://github.com/yurim22)


* 본격적인 분석에 들어가기 앞서 각 구역 별 치안안전등급 조사를 실시한다.

* `구역`의 범위는 각 지구대 및 파출소의 관할구역으로 지정한다.
   - 경찰청에서 요청하여 제공받은 '서울특별시 지방경찰청과 경찰서의 조직 및 사무분장규칙(법령전문)' 자료 참고

### 참고 자료 및 사이트

* 생활안전지도 

   - [홈페이지](https://www.safemap.go.kr/main/smap.do)
   
* 서울특별시 지방경찰청과 경찰서의 조직 및 사무분장규칙(법령전문)


### 📋데이터 수집

1. 생활안전지도의 치안안전 정보를 바탕으로 각 지역 별 5대범죄 및 전체 등급 수집

   > 5대범죄 : 살인, 강도, 절도, 폭력, 성폭력
   
   > 전체 등급 : 전체 범죄등급에 대한 평균
   
   * 범죄 정보 관련하여 여러 부정적인 영향이 있기 때문에 경찰청에서 자세하고 직접적인 범죄 데이터를 제공해주지 않는다.
   
   * 지도에서 하나하나 찾아가면서 엑셀에 정리
   
   * 생활안전지도에서 제공하는 치안안전등급 정보는 다음과 같다.
   
<img src="https://user-images.githubusercontent.com/33304898/82802455-e537d000-9eb9-11ea-8c7e-faa855157aee.png" width = 600, height = 300>
       
       
      - 생활안전지도에서 api형태가 아닌 png로 데이터를 제공해주기 때문에 직접 수집해야하는 어려움이 있었다.
       

2. 지구대 및 파출소 별 관할 구역 데이터 정리

   * 경찰청으로부터 제공받은 한글파일을 바탕으로 파출소 및 지구대 별 관할구역을 엑셀로 정리

3. 지구대 및 파출소 위도, 경도 데이터 추가

### 📋데이터 전처리

파출소 및 지구대 이름을 기준으로 직접 정리한 치안 안전 등급과 파출소 및 지구대 관할구역을 합쳐 하나의 파일로 생성 

1. 서울시 각 자치구의 범죄율 순위를 바탕으로 상위 8개의 구 조사 

    - [데이터보기](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/blob/master/yurim/02secure_data/secure_7.csv)
    - 중구
    - 종로구
    - 마포구
    - 영등포구
    - 용산구
    - 금천구
    - 강남구
    - 구로구
    
 2. 서울시 각 자치구의 범죄율 순위를 바탕으로 하위 6개의 구 조사
 
    - [데이터보기](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/blob/master/yurim/02secure_data/low_secure.csv)
    - 강서구
    - 양천구
    - 노원구
    - 성북구
    - 도봉구
    - 은평구


### 활용계획

* 지구대 및 파출소의 관할구역을 기준으로 구역을 나누어 범죄예방에 관련이 있다고 생각하는 요인들과 치안등급 간의 상관관계 분석

-------------------------------------------

## 분석2-1. cctv와 치안안전등급 간의 상관관계 분석

👤contributor

* [최리안](https://github.com/leeeeean)

### 📋데이터

#### 📋데이터 수집


**서울시 내 cctv 데이터

* 출처 : 공공데이터포털 
    - [데이터링크](https://www.data.go.kr/data/15013094/standard.do) 
    - 서대문구 제외 24개구의 cctv 데이터를 받아옴
    - 서대문구의 경우, 직접 데이터 요청을 통해 수집 완료


#### 📋데이터 전처리

* 공공데이터포털에서는 각 구별 cctv데이터 파일을 제공해주고 있어, 수집한 25개구의 데이터를 하나로 합침

* 결측치 제거

* 위도/경도 데이터 ➡️ 도로명주소 / 지번주소 데이터

* 도로명주소 / 지번주소 데이터 ➡️ 위도/경도 데이터

* 필요한 칼럼만 추출하여 저장 ([관리기관명, 카메라대수, 도로명주소, 지번주소, 위도, 경도])


### 상관관계 분석📊


* 범죄율 상위 8개구와 하위 6개 구에 대해서 분석 진행

* 각 파출소 및 지구대의 관할구역 데이터를 활용하여 각 구역 별 cctv의 수를 count

   - 파출소 및 지구대 관할구역 데이터 => [데이터](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/yurim/02secure_data)
   
   - dictionary 형태로 만들어 관할구역의 cctv 수를 나타냄
   
* cctv 개수 데이터와 치안등급 데이터 합치기(merge)

* 각 구역별 cctv 수와 치안등급 간의 상관분석 진행(corr 함수 사용)

### ✏️분석결과


**1. 범죄율 상위 8개 구**

![image](https://user-images.githubusercontent.com/33304898/82825268-e41c9800-9ee5-11ea-93fa-6aa8db7d9ebe.png)

* 전체적으로 거의 상관관계가 없어보임 

* 모든 범죄가 미약하지만 양의 상관관계를 갖는다.
 
 
 **2. 범죄율 하위 6개구**
 
 ![image](https://user-images.githubusercontent.com/33304898/82825291-f0085a00-9ee5-11ea-9c8f-7b6632c71c8d.png)
 
 * 전체적으로 양의 상관관계가 있는 것으로 보임
 
 * 특히 폭력과 성폭력의 경우 다른 범죄에 비해 확실한 양의 상관관계를 갖는다.

[데이터 전처리 및 분석 코드 바로가기](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/leean/01cctv_analysis)


--------------------------------------------

## 분석2-2. 보안등과 치안안전등급 간의 상관관계 분석

👤contributor

* [최리안](https://github.com/leeeeean)

### 📋데이터

#### 📋데이터 수집


**서울시 내 보안등 데이터

* 출처 : 공공데이터포털 / 서울열린데이터광장 
    - [데이터링크-공공데이터포털](https://www.data.go.kr/data/15013094/standard.do)
    - [데이터링크-서울열린데이터광장](https://data.seoul.go.kr/dataList/datasetList.do) 


#### 📋데이터 전처리

* 공공데이터포털 및 서울열린데이터광장에서는 각 구별 보안등 데이터 파일을 제공해주고 있어, 수집한 25개구의 데이터를 하나로 합침

* 결측치 제거

* 위도/경도 데이터 ➡️ 도로명주소 / 지번주소 데이터

* 도로명주소 / 지번주소 데이터 ➡️ 위도/경도 데이터

* 필요한 칼럼만 추출하여 저장 ([관리기관명, 카메라대수, 도로명주소, 지번주소, 위도, 경도])

### 상관관계 분석📊


* 범죄율 상위 8개구에 대해서 분석 진행

* 각 파출소 및 지구대의 관할구역 데이터를 활용하여 각 구역 별 보안등의 수를 count

   - 파출소 및 지구대 관할구역 데이터 => [데이터](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/yurim/02secure_data)
   
   - dictionary 형태로 만들어 관할구역의 보안등 수를 나타냄
   
* 보안등 수 데이터와 치안등급 데이터 합치기(merge)

* 각 구역별  수와 치안등급 간의 상관분석 진행(corr 함수 사용)


### ✏️분석결과


**1. 범죄율 상위 8개 구**

![image](https://user-images.githubusercontent.com/33304898/82825706-a8360280-9ee6-11ea-94f7-16b5a8730654.png)


* 거의 상관관계가 없는 것으로 보이는 결과가 나왔다.

* 하지만 상관관계의 부호가 – (마이너스)가 대부분으로 거의 상관관계는 없으나 미약한 음의 관계가 있다고 볼 수 있다.
 
* 다른 범죄에 비해서 절도의 경우에는 다른 범죄에 비해서 보안등과 더 음의 상관관계가 있다고 보여진다.

[데이터 전처리 및 분석 코드 바로가기](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/leean/02light_analysis)


---------------------------------------------

## 분석2-3. 경비인원 수와 치안안전등급 간의 상관관계 분석

👤contributor

* [배수혜](https://github.com/Uranel)

### 📋데이터

#### 📋데이터 수집

**1. 서울시 내 아파트 데이터

* 출처 : 서울열린데이터광장 
    - [데이터링크](http://data.seoul.go.kr/dataList/OA-15465/S/1/datasetView.do;jsessionid=8 F09D36EF9800C38BB3B39971C36D2D0.new_portal-svr-11#AXexec) 


#### 📋데이터 전처리

* 결측치 제거

* `경비인원` 칼럼의 값이 비어있는 경우, (아파트 동 수) * 2로 계산하여 데이터 보완

* 필요한 칼럼만 추출하여 저장 ([아파트명, 주소(시도), 주소(시군구), 주소(읍면동), 경비인원, 좌표 X, 좌표Y, 법정동주소, 단지분류, 도로명주소])

### 상관관계 분석📊


* 범죄율 상위 8개구와 하위 6개 구에 대해서 분석 진행

* 각 파출소 및 지구대의 관할구역 데이터를 활용하여 각 구역 별 경비인원 수를 count

   - 파출소 및 지구대 관할구역 데이터 => [데이터](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/yurim/02secure_data)
   
   - dictionary 형태로 만들어 관할구역의 경비인원 수를 나타냄
   
* 경비인원 수 데이터와 치안등급 데이터 합치기(merge)

* 각 구역별  수와 치안등급 간의 상관분석 진행(corr 함수 사용)

### ✏️분석결과


**1. 범죄율 상위 8개 구**

<img src="https://user-images.githubusercontent.com/33304898/82825779-cbf94880-9ee6-11ea-8239-cca624fe3e2f.png" width = 700 height = 350>
 
 * 전체적으로 약한 음의 상관관계를 가지고 있다.
 
 * 특히 폭력에서 음의 상관관계가 나타난다.
 
 
![image](https://user-images.githubusercontent.com/33304898/82825967-301c0c80-9ee7-11ea-9e52-eb352f8962aa.png)


 * 상관관계를 히트맵으로 시각화
 
 
 **2. 범죄율 하위 6개구**
 
<img src="https://user-images.githubusercontent.com/33304898/82826211-a882cd80-9ee7-11ea-8106-9855058cd53e.png" width=700 height=350>
 
 * 전체적으로 양의 상관관계를 가지고 있다/
 
![image](https://user-images.githubusercontent.com/33304898/82826305-d700a880-9ee7-11ea-8be3-04783d4920b3.png)

 * 상관관계를 히트맵으로 시각화

[데이터 전처리 및 분석 코드 바로가기](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/suhae)


---------------------------------------------

## 분석2-4. 파출소 수와 치안안전등급 간의 상관관계 분석

👤contributor

* [배수혜](https://github.com/Uranel)

### 📋데이터

#### 📋데이터 수집

**1. 서울시 내 파출소, 지구대, 치안센터, 경찰서 데이터

* 출처 : 공공데이터포털
    - [데이터링크](https://www.data.go.kr/dataset/3075501/fileData.do)


#### 📋데이터 전처리




### 상관관계 분석📊


* 범죄율 상위 8개구와 하위 6개 구에 대해서 분석 진행

* 각 파출소 및 지구대의 관할구역 데이터를 활용하여 각 구역 별 파출소 수를 count

   - 파출소 및 지구대 관할구역 데이터 => [데이터](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/yurim/02secure_data)
   
   - dictionary 형태로 만들어 관할구역의 파출소 수를 나타냄
   
* 경비인원 수 데이터와 치안등급 데이터 합치기(merge)

* 각 구역별  파출소 수와 치안등급 간의 상관분석 진행(corr 함수 사용)

### ✏️분석결과

![image](https://user-images.githubusercontent.com/33304898/82826660-8473bc00-9ee8-11ea-9bf5-8c9ae8c0172a.png)

* 치안센터의 수와 치안 등급과의 관계는 대부분 상관관계가 미미했으나 살인과 폭력에서는 0.5이상으로 확실한 양의 상관관계를 보였다.

* 분석의 의도는 치안 등급과 치안센터의 수의 관계가 음의 상관관계로 치안센터 개수가 많으면 등급이 낮아질 것으로 예상했으나 그와 다르게 상관관계가 거의 없거나 양의 상관관계가 보였다

* 상관 관계 분석으로는 인과 관계를 알 수는 없으므로 이 결과가 살인, 폭력이 많이 일어나서 치안센터가 많이 생기게 된 것인지 치안센터가 많아서 살인, 폭력사건이 많이 생긴 것인지 알 수 없다.

[데이터 전처리 및 분석 코드 바로가기](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/suhae)

-------------------------------------------

## 분석2-5. 근린시설과 치안안전등급 간의 상관관계 분석

👤contributor

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


### 📋데이터

👤유림 - `휴게음식점` `문화시설` 데이터 수집 및 전처리
👤희주 - `일반음식점` `공원` 데이터 수집 및 전처리


#### 📋데이터 수집


**1. 휴게음식점**

* 출처 : 서울열린데이터광장
    - [데이터링크](https://data.seoul.go.kr/dataList/OA-2347/S/1/datasetView.do)
* 위의 링크는 서대문구 휴게음식점 관련 데이터

* 이와 같이 각 구별 휴게음식점 데이터를 제공해주고 있어, 25개 구의 휴게음식점에 해당하는 데이터를 다운받아 전처리 진행

* 위도 / 경도 데이터가 없어 추가해야함

**2. 일반음식점**

* 출처 : 서울열린데이터광장
    - [데이터링크](https://data.seoul.go.kr/dataList/OA-10510/S/1/datasetView.do)
* 위의 링크는 은평구 일반음식점 관련 데이터

* 이와 같이 각 구별 일반음식점 데이터를 제공해주고 있어, 25개 구의 일반음식점에 해당하는 데이터를 다운받아 전처리 진행

* 위도 / 경도 데이터가 없어 추가해야함

**3. 문화시설**

* 출처 : 서울열린데이터광장
   - [데이터링크](https://data.seoul.go.kr/dataList/OA-13590/S/1/datasetView.do)
   
* 서울시 전체 문화시설 데이터 제공

* 주소 / 위도 / 경도 데이터 포함

**4. 공원**

* 출처 : 서울열린데이터광장
   - [데이터링크](https://data.seoul.go.kr/dataList/OA-394/S/1/datasetView.do)
   
   * 서울시 전체 공원 데이터 제공
   
   * 주소/위도/경도 데이터 포함
   


#### 📋데이터 전처리

**1. 휴게음식점 & 일반음식점**

* 폐업한 음식점까지 데이터에 포함되어 있어 폐업한 음식점 데이터는 삭제

* 중복되는 음식점 데이터 삭제

* 필요한 열만 뽑아서 저장

* 주소를 바탕으로 위도/경도로 변환시켜 데이터 추가

* 구별로 데이터 전처리를 진행하였는데, 이후 하나의 csv 파일로 합침

   - [관련코드](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/blob/master/yurim/03corr_neigh/data_preprocessing/code/union_df.py)
   
**2. 문화시설**

* 주소데이터가 비어있는 경우가 있어, 구글맵에서 찾아 주소 및 위도/경도 데이터 추가

**3. 공원**

* 필요한 열만 추출하여 

### 상관관계 분석📊

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

### ✏️분석결과


**1. 범죄율 상위 8개 구**


<img src = "https://user-images.githubusercontent.com/33304898/82792326-30e27d80-9eaa-11ea-84f6-d29c4bfeb5a9.png" width="600" height="300">

 * 절도, 폭력에서 약한 음의 상관관계를 보임
 
 * 하지만... 너무 약해서 문제
 
 
 **2. 범죄율 하위 6개구**
 
 <img src = "https://user-images.githubusercontent.com/33304898/82792843-fa593280-9eaa-11ea-8647-355705615174.png" width="600" height="300">

* 전반적으로 양의 상관관계를 갖는다

[데이터 전처리 및 분석 코드 바로가기1](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/yurim/03corr_neigh)
[데이터 전처리 및 분석 코드 바로가기1](https://github.com/MJU-Capstone-Design/FENCE_data_analysis/tree/master/heeju)
