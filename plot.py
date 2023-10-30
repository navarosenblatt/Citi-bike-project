maleRain = open("listMaleRain", "rt").readline()
line = maleRain.split("$")
ages = []
maleRainRiders = []*len(ages)
for i in line:
    field = i.split(",")
    if len(field)==2:
        age = int(field[0][4:-3])*5
        ages.append(str(age) + "-" + str(age+4))
        maleRainRiders.append(int(field[1][2:-2]))

maleDry = open("listMaleDry", "rt").readline()
line = maleDry.split("$")
maleDryRiders = []
for i in line:
    field = i.split(",")
    if len(field)==2:
        maleDryRiders.append(int(field[1][2:-2]))

femaleRain = open("listFemaleRain", "rt").readline()
line = femaleRain.split("$")
femaleRainRiders = []
for i in line:
    field = i.split(",")
    if len(field)==2:
        femaleRainRiders.append(int(field[1][2:-2]))

femaleDry = open("listFemaleDry", "rt").readline()
line = femaleDry.split("$")
femaleDryRiders = []
for i in line:
    field = i.split(",")
    if len(field)==2:
        femaleDryRiders.append(int(field[1][2:-2]))   
    
import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt

f = plt.figure()

N = len(ages)
index = np.arange(N)
width = .4

#malerain:
plt.bar(index, maleRainRiders, width, alpha= .8, color = "blue", label = "Male Precipitation")
#femalerain:
plt.bar(index+ width, femaleRainRiders, width, alpha= .8, color = "magenta", label = "Female Precipitation")

#maledry:
plt.bar(index, maleDryRiders, width, alpha= .4, color = "blue", label = "Male Dry", bottom = maleRainRiders)
#femaledry:
plt.bar(index+ width, femaleDryRiders, width, alpha= .4, color = "magenta", label = "Female Dry", bottom = femaleRainRiders)

plt.xlabel("Age and Gender")
plt.ylabel("# of Riders")
plt.title("Citi Bike Riders: \n Age, Gender, and Weather")
plt.xticks(index + width/2, ages)
plt.legend()

def calculate(mrain, mdry, frain, fdry):
    for i in range(len(ages)):
        mpercent = (mrain[i]*100)/(mrain[i] + mdry[i])
        fpercent = (frain[i]*100)/(frain[i] + fdry[i])
        #print(ages[i], mpercent, fpercent)
                                   
calculate(maleRainRiders, maleDryRiders, femaleRainRiders, femaleDryRiders)

plt.tight_layout()
plt.show()

f.savefig("plot.pdf")
