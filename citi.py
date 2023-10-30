citi = open("citibikedata/citiAll", "rt")
citi.readline()
g = open("citiidentity.txt", "wt")

for line in citi:
    print("here")
    field = line.split(",")
    if len(field)>14:
        starttime = field[1][1:-6]
        #start hour
        starthour = starttime[:13]+":00:00"
        try:
            birthyear= int(field[13])
        except:
            birthyear= None
        if not birthyear:
            continue
        age = 2018 - birthyear
        #age range
        ageRange = age//5
        sex= int(field[14])
        gender = None
        #assign gender
        if sex == 1:
            gender = "m"
        if sex == 2:
            gender = "f"
        if not gender:
            continue
        identity = str(ageRange) + "|" + gender
        g.write(starthour + "," + identity + "\n")          
g.close()
       
        
