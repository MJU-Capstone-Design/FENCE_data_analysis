setwd('C:/Users/Heejuu/Downloads/')
library("dplyr")

# 범죄율 상위 8개구
jung_r<- read.csv("서울시 중구 일반음식점 식품위생업소 현황.csv")
jung_r <- jung_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
jung_r = jung_r[!duplicated(jung_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(jung_r,file="jung_r.csv", row.names=FALSE)

jongno_r<- read.csv("서울시 종로구 일반음식점 식품위생업소 현황.csv")
jongno_r <- jongno_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
jongno_r = jongno_r[!duplicated(jongno_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(jongno_r,file="jongno_r.csv", row.names=FALSE)

mapo_r<- read.csv("서울시 마포구 일반음식점 식품위생업소 현황.csv")
mapo_r <- mapo_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
mapo_r = mapo_r[!duplicated(mapo_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(mapo_r,file="mapo_r.csv", row.names=FALSE)

ydp_r<- read.csv("서울시 영등포구 일반음식점 식품위생업소 현황.csv")
ydp_r <- ydp_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
ydp_r = ydp_r[!duplicated(ydp_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

yongsan_r<- read.csv("서울시 용산구 일반음식점 식품위생업소 현황.csv")
yongsan_r <- yongsan_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
yongsan_r = yongsan_r[!duplicated(yongsan_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

geumcheon_r <- read.csv("서울시 금천구 일반음식점 식품위생업소 현황.csv")
geumcheon_r <- geumcheon_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
geumcheon_r = geumcheon_r[!duplicated(geumcheon_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

gangnam_r <- read.csv("서울시 강남구 일반음식점 식품위생업소 현황.csv")
gangnam_r <- gangnam_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
gangnam_r = gangnam_r[!duplicated(gangnam_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

guro_r <- read.csv("서울시 영등포구 일반음식점 식품위생업소 현황.csv")
guro_r <- guro_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
guro_r = guro_r[!duplicated(guro_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

df = rbind(jung_r, jongno_r, mapo_r, ydp_r, yongsan_r, geumcheon_r, gangnam_r, guro_r)
write.csv(df,file="df_seoul_restaurant_h.csv", row.names=FALSE)

# 범죄율 하위 6개구
yp_r<- read.csv("서울시 은평구 일반음식점 식품위생업소 현황.csv")
yp_r <- yp_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
yp_r = yp_r[!duplicated(yp_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(mapo_r,file="mapo_r.csv", row.names=FALSE)

dobong_r<- read.csv("서울시 도봉구 일반음식점 식품위생업소 현황.csv")
dobong_r <- dobong_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
dobong_r = dobong_r[!duplicated(dobong_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

sb_r<- read.csv("서울시 성북구 일반음식점 식품위생업소 현황.csv")
sb_r <- sb_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
sb_r = sb_r[!duplicated(sb_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

nowon_r <- read.csv("서울시 노원구 일반음식점 식품위생업소 현황.csv")
nowon_r <- nowon_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
nowon_r = nowon_r[!duplicated(nowon_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

yangcheon_r <- read.csv("서울시 양천구 일반음식점 식품위생업소 현황.csv")
yangcheon_r <- yangcheon_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
yangcheon_r = yangcheon_r[!duplicated(yangcheon_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

gangseo_r <- read.csv("서울시 강서구 일반음식점 식품위생업소 현황.csv")
gangseo_r <- gangseo_r %>% filter(is.na(폐업일자)) %>% select(업소일련번호, 업소명, 소재지도로명, 소재지지번, 행정동명, 허가.신고.번호)
gangseo_r = gangseo_r[!duplicated(gangseo_r[,c('업소일련번호','허가.신고.번호')]),]
#write.csv(ydp_r,file="ydp_r.csv", row.names=FALSE)

df1 = rbind(yp_r, dobong_r, sb_r, nowon_r, yangcheon_r, gangseo_r)
write.csv(df1,file="df_seoul_restaurant_l.csv", row.names=FALSE)

setwd('C:/work/capstone/correlation')
library("dplyr")

restaurant_l <- read.csv("df_seoul_restaurant_l.csv")
restaurant_h <- read.csv("df_seoul_restaurant_h.csv")
rest_l <- read.csv("df_rest_restaurant_l.csv")
rest_l <- rest_l %>% select(업소명, 소재지도로명, 소재지지번, 행정동명)
rest_h <- read.csv("df_rest_restaurant_h.csv")
rest_h <- rest_h %>% select(업소명, 소재지도로명, 소재지지번, 행정동명)
df2 = rbind(restaurant_h, restaurant_l)
write.csv(df2, file="df_seoul_restaurant.csv", row.names=FALSE)
df3 = rbind(rest_h,rest_l)
write.csv(df2, file="df_rest_restaurant.csv", row.names=FALSE)
