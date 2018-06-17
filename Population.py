from Chromosome import Chromosome
import random

class Population():
    def __init__(self, dim, numOfGen):
        self.__dimension = dim
        self.__numOfGen = numOfGen

        self.__population = []


    def initPop(self):
        for i in range(0, self.__dimension):
            self.__population.append(Chromosome())


    def fitPop(self):
        for i in range(0, self.__dimension):
            self.__population[i].evalCromozom(400,500,200,3,10)


    def getBest(self):
        bestCr = Chromosome()
        bestCr.setFitness(1000000)
        for i in range(1, self.__dimension):
            if bestCr.getFitness() > self.__population[i].getFitness() and self.__population[i].getFitness() >= 1 and self.__population[i].getTime() >=3000:
                bestCr = self.__population[i]
        
        return bestCr


    def getNumOfGen(self):
        return self.__numOfGen
    def getDim(self):
        return self.__dimension


    def setPop(self, pop):
        for i in range(0, self.__dimension):
            self.__population[i] = pop[i]


    def selection(self):
        pos1 = random.randint(0, self.__dimension-1)
        pos2 = random.randint(0, self.__dimension-1)

        if(self.__population[pos1].getFitness() < self.__population[pos2].getFitness()):
            return self.__population[pos1]
        return self.__population[pos2]


    def xo(M, F):
        c = Chromosome()

        # set weights IH for xo
        for i in range(0, M.getDimensionWeightsIH()[0]):
            for j in range(0, M.getDimensionWeightsIH()[1]):
                r = random.uniform(0,1)
                if r < 0.5:
                    c.setWeightsIHPos(i,j,M.getWeightsIHPos(i,j))
                else:
                    c.setWeightsIHPos(i,j,F.getWeightsIHPos(i,j))


        # set weights HO for xo
        for i in range(0, M.getDimensionWeightsHO()[0]):
            l = []
            for j in range(0, M.getDimensionWeightsHO()[1]):
                r = random.uniform(0,1)
                if r < 0.5:
                    c.setWeightsHOPos(i,j,M.getWeightsHOPos(i,j))
                else:
                    c.setWeightsHOPos(i,j,F.getWeightsHOPos(i,j))
        return c

    def mutation(c):
        for i in range(0, 10):
            posI = random.randint(0, 5)
            posJ = random.randint(0, 11)
            c.setWeightsIHPos(posI, posJ, c.getWeightsIHPos(posI, posJ) + random.uniform(-0.2,0.2))

        for i in range(0, 5):
            posI = random.randint(0, 4)
            posJ = random.randint(0, 5)
            c.setWeightsHOPos(posI, posJ, c.getWeightsHOPos(posI, posJ) + random.uniform(-0.2,0.2))
        return c


