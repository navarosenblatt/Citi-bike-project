f = open("weatherdata/weather2018", "rt")
f.readline()

g = open("precipitation.txt", "wt")

for line in f:
        field = line.split("|")
        dateTime = field[1][:19]
        if dateTime.split()[0].split("-")[0] == "2018":
                if field[30]== "Rain" or field[30]=="Snow":
                        g.write(dateTime + "\n")
                       
                    
      
          

     
  

