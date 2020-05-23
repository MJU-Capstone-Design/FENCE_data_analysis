# 서울시 내 자치구 범죄율 순위 분석

### 활용한 데이터

* 서울시 관서별 5대범죄
   - 출처 : 공공데이터 포털 
   - [홈페이지](https://www.data.go.kr/data/15054737/fileData.do)

* 서울시 인구분포
   - 출처 : 국가통계포털 
   - [홈페이지](http://kosis.kr/index/index.do)
   
   
## 분석 방법
> 범죄율=(형법범죄 / 총인구) ×  100,000

* 서울시 자치구별 발생한 5대범죄 건수를 파악하고 총 범죄 발생 건수를 구한다.
* 범죄율 구하는 공식에 따라 범죄 발생건수를 자치구 인구 수로 나누어 주고 100000을 곱한다.
* 인구 십만명 당 발생하는 범죄 건수를 구하여 sorting한다.

1. 범죄율 순위 결과(table)

![범죄율 순위표](https://user-images.githubusercontent.com/33304898/82736405-8a409480-9d64-11ea-94ef-3ebe06b204ec.JPG)

2. 범죄율 시각화(plot)

<img src="https://user-images.githubusercontent.com/33304898/82736505-397d6b80-9d65-11ea-9662-6f6220218295.JPG"  width="600" height="370">
