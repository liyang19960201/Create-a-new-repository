import numpy as np


print("game start")
A = np.random.uniform(0,1,size = (10**6,10**3))
B = np.random.uniform(0,1,size = (10**3,10**6))
C=np.random.uniform(0,1,size = (10**6,1))


D=np.dot(A,B)
   
E=np.dot(D,C)

i=0
while i<10:

    print(f"The {i+1}th of metrix E is:{E[i]}")
    i+=1