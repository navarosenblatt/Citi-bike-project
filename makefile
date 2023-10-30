all: plot.txt

citiAll: JC-201801-citibike-tripdata.csv.zip JC-201802-citibike-tripdata.csv.zip \
JC-201803-citibike-tripdata.csv.zip JC-201804-citibike-tripdata.csv.zip \
JC-201805-citibike-tripdata.csv.zip JC-201806-citibike-tripdata.csv.zip \
JC-201807-citibike-tripdata.csv.zip JC-201808-citibike-tripdata.csv.zip \
JC-201809-citibike-tripdata.csv.zip JC-201810-citibike-tripdata.csv.zip \
JC-201811-citibike-tripdata.csv.zip JC-201812-citibike-tripdata.csv.zip
	zcat citibikedata/JC-2018* > citiAll 

weather2018: manhattanWeatherClean.gz
	zcat weatherdata/manhattanWeatherClean.gz | grep 2018 > weather2018

precipitation.txt: weather.py weather2018
	python3 weather.py

citiidentity.txt: citi.py citiAll
	python3 citi.py

buckets.txt: buckets.py precipitation.txt citiidentity.txt
	python3 buckets.py


listMaleRain listMaleDry listFemaleRain listFemaleDry: sortbuckets.py buckets.txt
	python3 sortbuckets.py

plot.txt: plot.py listMaleRain listMaleDry listFemaleRain listFemaleDry
	python3 plot.py


clean:
	rm citiAll weather2018 precipitation.txt citiidentity.txt buckets.txt\
listMaleRain listMaleDry listFemaleRain listFemaleDry plot.txt
