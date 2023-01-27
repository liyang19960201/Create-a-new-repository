Multiply the three matrices: A, B, and C;  i.e., you are expected to find the matrix D where D=(A*B)*C. 
A, B, and, C contain random numbers in the range of (0,1) and the dimensions of the matrices are as follows. 
A is a matrix with dimension 10^6 x 10^3 
B is a matrix with dimension 10^3  x 10^6 
C is a matrix with dimension 10^6  x 101




1.  Availability. A URL for the source code where your code is available. Please ensure that the code is documented.(0.5 point) 

The code is stored in a repository in GitHub, which you can find by accessing https://github.com/liyang19960201/Create-a-new-repository.git



2. Programming Language. Details on the choice of programming language you used, and the libraries. (0.5 point) 

The programming language I chose is python with lines of code to execute the function to generate three matrices as question required.

The library I applied is NumPy, which is the fundamental package for scientific computing in python, which allows to generate three matrices with random numbers and defined shapes.

The another library to plot the cumulative distribution function was matplotlib.pyplot as the plot to generate the graphic based on matrix A.



3. Methodology.  Details of how the matrix are created and multiplied, and the techniques for evaluating the performance. (2 points).

1.	The matrices were created by np.random.uniform(0,1, size=(10**6, 10**3)), which represents that it creates a matrix with value between 0 and 1 for each elements with float numbers because I used uniform.
2.	The multiplication was applied with np.dot (matrix 1, matrix 2), it is also possible to create a function to multiply two metrices but as for this document, the solution is np.dot ()
3.	There two technics and one evaluation for this question, the first technic is that np.dot () can determine if two metrices are eligible to multiply.
 
4.	The second technic is that to reach the result with product of matrices, the method is using two products of metrices A and B to middle matrix E, and the multiplication of E and C to get targeting matrix D.



4. Dataset. Plot a (empirical) cumulative distribution function (CDF) of all the values present in matrix A. What can you infer from the CDF? (2 points)

The cumulative distribution functions were displayed down below as matrix A with input. It goes with function histogram from numpy library to collect the frequencies of values based on elements from matrix A. The X-axile represent the defined value between 0 and 1, the y-axile was the frequency of cumulative values.
 
Figure 4-1 CDF Plot Based on Matrix A

From this graphic, I can infer that their value appeared from matrix A is between 0 AND 1 because it was how it was required from question and was defined from my code. Another thing is that the sum of those values is closer to 1 when the based value is near 10**9, because the sum of bigger numbers is larger. Finally, the cumulative frequency shows linear relationship with values in matrix. (This is the result after server runs and it remains same shape)


5. Evaluation. Plot the time evolution of the memory usage, and CPU (and/or GPU) usage of your solution. What do you infer from the plots? (2 points)

To demonstrate the monitoring status better, there is a screen recording during the code was executing, accidently it was contained with environment noise, it is recommended to watch with mute. https://youtu.be/GZq_66Bzu_A

Nerveless, when the program was launched, there is a rapid spike from memory usage, but CPU doesn’t indicate that intensive load with some obvious increase in loading tasks. Then, it becomes a slightly slow but start rising again for the memory usage until Visual Code gives “Killed: 9” with almost full utilization of memory and this task was released, the usage intended to back where it was before the code was running.

In later test, it can lead to full ram situation force thermal engages to kill this process eventually.

6. Discussion. Detail the various challenges encountered and how you addressed those challenges. If you are unable to obtain D, what is the largest size of the matrices for which you were able to compute D.  (3 points)

challenge1: It takes some time to get used with matrix in python since I only had experience with matrix mathematically.
Challenge 2: It is impossible to reach a reasonable result from laptop eventually lead to full ram and overheating condition. I tried to use Puhti supercomputer Visual Studio Editor, but it doesn’t support numpy and matplotlib libraries for some reasons, and I have not any access to install those modules also.

Challenge 3: I don’t get familiar with CDF, and I made some researches on the definition and how to get it from a matrix. There are also different methods to display CDF, but I chose to use histogram eventually to reach the result.

Challenge 4: Fortunately, I learned how to use GitHub from last semester, and it is a fantastic opportunity to build a repository and commit some changes to codes once again.

With several try, the biggest matrix I can reach from my laptop is approximate:


A = np.random.uniform(0,1,size = (10**4,10**3))
B = np.random.uniform(0,1,size = (10**3,10**4))
C=np.random. uniform(0,1,size = (10**4,1))

With this running, I can receive the result: (I only print out the first six elements for verification purposes)

(base) MacBook-Pro:~ yangli$ /Users/yangli/opt/anaconda3/bin/python /Users/yangli/Desktop/test.py
game start
the 0 elements in D is [1265173.21402759]
the 1 elements in D is [1213036.80215849]
the 2 elements in D is [1254670.12267548]
the 3 elements in D is [1228600.07827866]
the 4 elements in D is [1268386.3383631]
the 5 elements in D is [1244230.39811832]

It is noticed that a matrix with dimension of 100,000 requires around 74.5GB of RAM, with the question has 1,000,000 x 1000 is obviously beyond the capacity of my laptop at least.

