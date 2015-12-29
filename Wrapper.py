'''
Created on Mar 2, 2015

@author: Saurav

'''
import collections
import matplotlib.pyplot as plt
import Simulation1 as s1
#import Simulation2 as s2
import random
from audioop import avg

s1arr = []
#s2arr = []
for i in range(100):
    n= 30
    m = 3.0
    #n=10
    #m=40
    k=0.05
    s1KappaArr = {}
 #   s2KappaArr = {}
    while (True):

        val1=s1.mainCall(n, m, k)
        s1KappaArr[k] = len(val1)
  #      val2=s2.mainCall(n,m,k)
  #      s2KappaArr[k] = len(val2)
        k += 0.05
        if k >=1:
            break

    s1arr.append(s1KappaArr)
   # s2arr.append(s2KappaArr)
#print s1arr

k=0.05
od = {}
s1KappaAvgVector = {}
s1Kappa=[]
while True:
    sum = 0
    for i in range(100):
        #print s1arr[i][k]
        sum += s1arr[i][k]

    avg = float(sum)/100.0
    s1KappaAvgVector[k] = avg
    s1Kappa.append(k)
    k +=0.05
    if k>1:
        break


print s1KappaAvgVector
od = collections.OrderedDict(sorted(s1KappaAvgVector.items()))
print od 
plt.plot(s1Kappa,od.values())
plt.axis([0,1,0,30])
plt.show()
