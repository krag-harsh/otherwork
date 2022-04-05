import pandas as pd
from statistics import stdev
from statistics import mean
from statistics import median
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('nback2.data.2021-02-21--17-57.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

matchdata=data[4].to_numpy()
falsedata=data[6].to_numpy()
reactiontime=data[7].to_numpy()

#---------part 3 of question----------

reacttime1=[]
reacttime2=[]
for i in range(len(matchdata)):
    if(matchdata[i]==1):
        reacttime1.append(data[7][i])
    if(falsedata[i]==1):
        reacttime2.append(data[7][i])

x=['Match trial', 'False alarm']
y=[mean(reacttime1),  mean(reacttime2)]
z=[stdev(reacttime1), stdev(reacttime2)]
plt.bar(x, y, yerr=z)
plt.ylabel("Reaction time in millisecond")
plt.title("Question 2 part C")
plt.show()

#---------part 4 of question----------

FH, SH=0 , 0
FHm, SHm=0 , 0
retime=[]
#here we are not considerign reactiontime with 3000 as it is the case when the subject didn't respond anything
for i in range(len(reactiontime)):
    if(reactiontime[i]!=3000):
        retime.append(reactiontime[i])


medR=median(retime)
#we know that for reactiontime of 3000 match value is 0 always
for i in range(len(reactiontime)):
    if(reactiontime[i]!=3000):
        if(reactiontime[i] <= medR):
            FH+=1
            if(matchdata[i]==1):
                FHm+=1
        else:
            SH += 1
            if (matchdata[i] == 1):
                SHm += 1
print("Percentage of match trials in First half of median of reaction time :",FHm/FH*100)
print("Percentage of match trials in Second half of median of reaction time :",SHm/SH*100)
