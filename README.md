# Citi-bike-project

Hypothesis: Males between the ages of 20-24 are the most likely to use Citi Bike in the rain/snow. 

Summary: To test this hypothesis, I used Citi Bike data from 2018 (which includes start time, age, and gender of each ride), and crossed it with weather data from 2018. For each ride, I checked whether there was precipitation at the start of the ride, and added to a count of that age range, gender, and weather.

I used the weather data to create a file of weather for 2018.

I compiled the Citi Bike data per month of 2018 into one file.

Weather.py- I used the weather 2018 data to write all of the rainy datetimes to a new file called precipitation.txt. 

Citi.py- I looped through each line in the citi data and got the start hour, age, and gender of each ride, and wrote it to a file called citiidentity.txt.

Buckets.py- I used precipitation.txt to make a dictionary of the rainy datetimes. I then looped through each line in citiidentity.txt and checked if the start hour was in the rainy dictionary. Then I incremented the count of the appropriate age, gender, and weather in a dictionary called buckets. Finally, I looped through the buckets dictionary and wrote the age, gender, weather, and count to a file called buckets.txt.
 
Sortbuckets.py- This program reads from buckets.txt and filters and sorts the buckets. I then wrote the sorted counts of the number of riders in each age range, gender, and weather
to 4 files called listMaleRain, listMaleDry, listFemaleRain, listFemaleDry. 

Plot.py- This program reads from the previous 4 files and makes a list of the counts for each, as well as a list of the age ranges. I then graphed the resulting lists in bar graph format, and created plot.pdf. 

Conclusion: My hypothesis proved to be marginally true. I found that the percentage of Citi Bike riders in precipitation compared with total riders was very similar for each age range and gender. However, the percentage for males between 20-24 was indeed the highest, winning by about 1%. I also found that males in general are around 1% more likely to ride in the rain than females, and that male Citi Bike riders make up around 75% of total riders, while female Citi Bike riders make up the other 25%. I printed this information to stdout. 
