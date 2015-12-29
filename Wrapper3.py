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
    n= 30
    m = 0.05
    #n=10
    #m=40
    k=0.95
    s1KappaArr = {}
 #   s2KappaArr = {}
    while (True):

        val1=s1.mainCall(n, m, k)
        s1KappaArr[m] = len(val1)
  #      val2=s2.mainCall(n,m,k)
  #      s2KappaArr[k] = len(val2)
        m += 0.05
        if m >=1:
            break

    s1arr.append(s1KappaArr)
   # s2arr.append(s2KappaArr)
#print s1arr

m=0.05
od = {}
s1KappaAvgVector = {}
s1Kappa=[]
while True:
    sum = 0
    for i in range(50):
        #print s1arr[i][k]
        sum += s1arr[i][m]

    avg = sum/50.0
    s1KappaAvgVector[m] = avg
    s1Kappa.append(m)
    m +=0.05
    if m>=1:
        break


print s1KappaAvgVector
od = collections.OrderedDict(sorted(s1KappaAvgVector.items()))
print od 
plt.plot(s1Kappa,od.values())
plt.axis([0,1,0,30])
plt.show()
