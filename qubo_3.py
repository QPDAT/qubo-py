import openjij as oj

#AND 00 , 10 , 01
Q = {(0, 0): 0, (0, 1): 1/2, (1, 0): 1/2, (1, 1): 0}
sampler = oj.SASampler()
response = sampler.sample_qubo(Q)
print(response.states)

#OR 00
Q = {(0, 0): 1, (0, 1): -1/2, (1, 0): -1/2, (1, 1): 1}
sampler = oj.SASampler()
response = sampler.sample_qubo(Q)
print(response.states)

#XOR 00 , 11
Q = {(0, 0): 1, (0, 1): -1, (1, 0): -1, (1, 1): 1}
sampler = oj.SASampler()
response = sampler.sample_qubo(Q)
print(response.states)