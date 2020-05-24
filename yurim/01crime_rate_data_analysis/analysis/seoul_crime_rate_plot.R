data <- read.csv("../capstone_design/seoul_crime_rate.csv", header = TRUE)

data <- data[-26,c(-1)]
data

install.packages("ggplot2")
install.packages("ggmap")
install.packages("raster")
library(ggmap)
library(raster)

install.packages("maptools")
library(maptools)
install.packages("gpclib")

install.packages('rgeos')
install.packages('rgdal')
library(rgdal)
library(ggplot2)
library(rgeos)


korea <- shapefile("./SIG_201905/TL_SCCO_SIG.shp")
ggplot() + geom_polygon(data=korea, aes(x=long, y=lat, group=group), fill='white', color='black')
head(korea)
korea <- fortify(korea, region='SIG_CD')
head(korea)

seoul <- korea[korea$id <= 11740, ]
ggplot() + geom_polygon(data=seoul, aes(x=long, y=lat, group=group), fill='white', color='black')

seoul <- merge(seoul, data, by="id")
head(seoul)
ggplot() + geom_polygon(data = seoul, aes(x = long, y = lat, 
                   group = group, fill = crime_rate),color = "white")  + 
  scale_fill_gradient(low = "#F7D343",
                      high = "#DB1212",
                      space = "Lab",
                      guide = "colourbar") +
  labs(fill = "¹üÁËÀ²") +
  theme_void() +
  theme(legend.position = c(.15, .85))
