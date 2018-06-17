from Population import Population
import random


def printFileBest(chr, i):
    fFit = open("fitness.txt", "a")
    file = "result" +  str(i) + ".txt"
    f = open(file, "w")
    
    fFit.write("gen " + str(i)+ ":   fit- " + str(chr.getFitness()) + "     time- " +str(chr.getTime()))
    fFit.write("\n")

    for i in range(chr.getDimensionWeightsIH()[0]):
        for j in range(chr.getDimensionWeightsIH()[1]):
            f.write(str(chr.getWeightsIHPos(i,j))+",")
        f.write("\n")

    f.write("\n")
    for i in range(chr.getDimensionWeightsHO()[0]):
        for j in range(chr.getDimensionWeightsHO()[1]):
            f.write(str(chr.getWeightsHOPos(i,j))+",")
        f.write("\n")

    print(chr.getFitness())

    fFit.close()
    f.close()



def train():
    p = Population(60, 40)   

    p.initPop()

    for i in range(0, p.getNumOfGen()):
        print("\nGENERATIA  ", i)
        p.fitPop()
        printFileBest(p.getBest(), i)
        popAux = []
        for j in range(0, p.getDim()):
               
            M = p.selection()
            F = p.selection()

            xo = Population.xo(M,F)

            prob = random.uniform(0,1)
            if(prob <= 0.2):
                xo = Population.mutation(xo)
            
            popAux.append(xo)
        p.setPop(popAux)
        
    p.fitPop()

    

train()
