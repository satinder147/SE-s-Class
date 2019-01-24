import random

class dna:
    def __init__(self,x):
        self.f=None
        self.target="TO BE OR NOT TO BE"
        self.phrase=""
        if(x==1):
            for _ in range(len(self.target)):
                self.phrase+=chr(random.randrange(32,90))
    def fitness(self):
        j=0
        for i in  range(len(self.target)):
            if(self.target[i]==self.phrase[i]):
                j=j+1
        self.f=j/len(self.target)

    def cross(self,a,b,rate):
        child=dna(0)
        mid=int(random.randrange(len(self.target)))
        for i in range(len(self.target)):
            if(i<mid):
                if(random.uniform(0,1)<rate):
                    child.phrase+=chr(random.randrange(32,90))
                else:
                    child.phrase+=a.phrase[i]
            else:
                    if(random.uniform(0,1)<rate):
                        child.phrase+=chr(random.randrange(32,90))
                    else:
                        child.phrase+=b.phrase[i]
        return child
