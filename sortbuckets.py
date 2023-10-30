import pyspark

def getFields(x):
    fields = x.split(',')
    identity = fields[0]
    count = fields[1]
    return (identity, count)

sc = pyspark.SparkContext()
sc.setLogLevel("ERROR")

a = sc.textFile('buckets.txt')
b = a.map(getFields)

male =   b.filter(lambda x: x[0].split("|")[2]=="m" and int(x[0].split("|")[1])<14 and int(x[0].split("|")[1])>3)

c = male.filter(lambda x: x[0].split("|")[0]=="1")
malerain = c.sortBy(lambda x: int(x[0].split("|")[1])).collect()

d = male.filter(lambda x: x[0].split("|")[0]=="0")
maledry = d.sortBy(lambda x: int(x[0].split("|")[1])).collect()


female =   b.filter(lambda x: x[0].split("|")[2]=="f" and int(x[0].split("|")[1])<14 and int(x[0].split("|")[1])>3)

e = female.filter(lambda x: x[0].split("|")[0]=="1")
femalerain = e.sortBy(lambda x: int(x[0].split("|")[1])).collect()

g = female.filter(lambda x: x[0].split("|")[0]=="0")
femaledry = g.sortBy(lambda x: int(x[0].split("|")[1])).collect()
                

mrain = open("listMaleRain", "wt")
for i in malerain:
    mrain.write(str(i) + "$")
mrain.close()

mdry = open("listMaleDry", "wt")
for i in maledry:
    mdry.write(str(i) + "$")
mdry.close()


frain = open("listFemaleRain", "wt")
for i in femalerain:
    frain.write(str(i) + "$")
frain.close()

fdry = open("listFemaleDry", "wt")
for i in femaledry:
    fdry.write(str(i) + "$")
fdry.close()




