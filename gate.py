#import items
import numpy as np
import openjij
from openjij import SQASampler
#make a 3d matrix as QUBO's coefficients
N = 3
OBJAND = np.zeros(N**2).reshape(N,N)
OBJOR = np.zeros(N**2).reshape(N,N)
#for QUBO which describes OR gate Q(ii)'s are one 
for i in range(N):
    OBJOR[i][i]=1
#insert the coefficients of QUBOs 
OBJAND[0][1]=1
OBJAND[0][2]=-2
OBJAND[1][2]=-2
OBJAND[2][2]=3
OBJOR[0][1]=1
OBJOR[0][2]=-2
OBJOR[1][2]=-2

sampler = SQASampler()
Nsample = 100
samplesetAND = sampler.sample_qubo(OBJAND, num_reads=Nsample)
samplesetOR = sampler.sample_qubo(OBJOR, num_reads=Nsample)
print(samplesetAND)
print(samplesetOR)
# I could not find an argument that changes the labels of this sampler so you most know first one is AND gate and the second one is OR gate.
