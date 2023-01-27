import numpy as np
import matplotlib.pyplot as plt




print("game start")
A = np.random.uniform(0,1,size = (10**6,10**3))
B = np.random.uniform(0,1,size = (10**3,10**6))
C=np.random.uniform(0,1,size = (10**6,10**1))


values, base = np.histogram(A, bins=40)
cumulative = np.cumsum(values)

plt.plot(base[:-1], cumulative, c='blue')
plt.xlabel("Values")
plt.ylabel("Cumulative Frequency")
plt.title("Empirical CDF of values in matrix A")
plt.show()

E=np.dot(A,B)
   
D=np.dot(E,C)

i=0

while i<6:
   print(f"the {i} elements in D is D[i]")
   i+=1
  
