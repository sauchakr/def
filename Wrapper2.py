'''
Created on Mar 14, 2015

@author: Saurav
'''
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
for i in range(50):
    n= 10
    m = 3.0
    #n=10
    #m=40
    k=0.95
    s1KappaArr = {}
 #   s2KappaArr = {}
    while (True):

        val1=s1.mainCall(n, m, k)
        s1KappaArr[n] = len(val1)
  #      val2=s2.mainCall(n,m,k)
  #      s2KappaArr[k] = len(val2)
        n += 10
        if n >=100:
            break

    s1arr.append(s1KappaArr)
   # s2arr.append(s2KappaArr)
#print s1arr

n=10
od = {}
s1KappaAvgVector = {}
s1Kappa=[]
while True:
    sum = 0
    for i in range(50):
        #print s1arr[i][k]
        sum += s1arr[i][n]

    avg = sum/50.0
    s1KappaAvgVector[n] = avg
    s1Kappa.append(n)
    n +=10
    if n >= 100:
        break


print s1KappaAvgVector
od = collections.OrderedDict(sorted(s1KappaAvgVector.items()))
print od 
plt.plot(s1Kappa,od.values())
plt.axis([0,100,0,100])
plt.show()
