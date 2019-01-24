import random
from cl import dna

population=[]

for _ in range(200):
    population.append(dna(1))
print(population[0].phrase)
g=0
f=False
while 1:
    g=g+1
    for i in range(200):
        population[i].fitness()
    pool=[]
    for i in range(200):
        n=int(population[i].f*100)
        for _ in range(n):
            pool.append(population[i])

    for i in range(200):
        a=random.randrange(len(pool))
        b=random.randrange(len(pool))
        population[i]=population[i].cross(pool[a],pool[b],.1)
        print(population[i].phrase)
        if(population[i].phrase=="TO BE OR NOT TO BE"):
            f=True
            break
    if(f):
        break
print(g)
