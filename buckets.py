precip = open("precipitation.txt")
precip.readline()
d = {}
for line in precip:
    line = line.strip()
    d[line]= ""

citi = open("citiidentity.txt", "rt")
citi.readline()

buckets = {}
for line in citi:
    field = line.split(",")
    starthour = field[0]
    identity = field[1]
    #print(identity)
    if starthour in d:
        identity = "1" + "|" + identity
        #print(identity)
        if not identity in buckets:
            buckets[identity]=1
        else:
            buckets[identity]+=1
    else:
        identity = "0" + "|" + identity
        if not identity in buckets:
            buckets[identity]=1
        else:
            buckets[identity]+=1
    #print(identity)
                    
g= open("buckets.txt", "wt")

for i in buckets:
    num =  str(buckets[i])
    key = i.strip()
    g.write(key + "," +  num + "\n")
  



