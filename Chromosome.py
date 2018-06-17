from NeuralNetwork import NeuralNetwork
import random


class Chromosome():
    def __init__(self):
        # 10 inputs - 1 =  distance from elem to leftLimit
        #             2 =  distance from elem to upLimit
        #             3 =  distance from elem to rightLimit
        #             4 =  distance from elem to downLimit
        #             5 =  distance from elem to first opponent  ( X axis)
        #             6 =  distance from elem to first opponent ( Y axis)
        #             7 =  distance from elem to second opponent ( X axis)
        #             8 =  distance from elem to second opponent ( Y axis)
        #             9 =  distance from elem to third opponent ( X axis)
        #             10 = distance from elem to third opponent ( Y axis)
        #             11 = speed
        #             12 = dimension
        

        # 8 hidden
        # 5 outputs - 1  = move to up
        #             2  = move to right
        #             2  = move to right
        #             3  = move to down
        #             4  = move to left
        #             5  = stay
        # 
        self.__nn = NeuralNetwork(12 , 8, 5)
        self.__time = 0
        # fitness is how long "time" elem survive
        self.__fitness = 0

    def getFitness(self):
        return self.__fitness
    def getTime(self):
        return self.__time
    def setFitness(self, f):
        self.__fitness = f

    def getWeightsIHPos(self, posI, posJ):
        return self.__nn.getWeightsIHPos(posI, posJ)
    def getWeightsHOPos(self, posI, posJ):
        return self.__nn.getWeightsHOPos(posI, posJ)

    def getDimensionWeightsIH(self):
        return self.__nn.getDimensionWeightsIH()
    def getDimensionWeightsHO(self):
        return self.__nn.getDimensionWeightsHO()

    def setWeightsIHPos(self, posI, posJ, val):
        self.__nn.setWeightIHPos(posI, posJ, val)
    def setWeightsHOPos(self, posI, posJ, val):
        self.__nn.setWeightHOPos(posI, posJ, val)

    


    def evalCromozom(self, winWidht, winHeight, winMiddleLimit, speed, dimension):

        opponents = []
        opponents.append([random.randint(1, winWidht), random.randint(1, winMiddleLimit)])
        opponents.append([random.randint(1, winWidht), random.randint(1, winMiddleLimit)])
        opponents.append([random.randint(1, winWidht), random.randint(1, winMiddleLimit)])

        xAI = winWidht//2
        yAI = winHeight//2 + winHeight//4

        t = 0
        numberOfMoves = 1
        crash = False
        numberOfOpponent = 3


        # simulate the game while AI is alive
        while not crash:
                
            # if is opponent in table
            # create the inputs for neuralNetwork( time t)
            inputs = []
            inputs.append(xAI + dimension//2)                    # distance from leftLimit to AI
            inputs.append(yAI + dimension//2 - winMiddleLimit)   # distance from middleLimit to AI
            inputs.append(winWidht - xAI + dimension//2)         # distance from AI to rightLimit
            inputs.append(winHeight - yAI + dimension//2)        # distance from AI to downLimit

            for i in range(0, len(opponents)):
                inputs.append(xAI - opponents[i][0])     # x - distance from opponent i to AI  
                inputs.append(yAI - opponents[i][1])     # y - distance from opponent i to AI
               
            inputs.append(speed)
            inputs.append(dimension)

            # receive the output from NeuralNetwork
            outputs = self.__nn.feedForward(inputs)
               
                
            posMove = 0
            valMove = 0
            for i in range(0,len(outputs)):
                if outputs[i] > valMove:
                    valMove = outputs[i]
                    posMove = i

            # move opponent
            for i in range(0, len(opponents)):
                if opponents[i][0] != 0:
                    opponents[i][1] += speed
                
            # move AI
            if posMove == 0:
                if yAI - speed >= winMiddleLimit:
                    yAI -= speed
                    numberOfMoves += 1
            if posMove == 1:
                if xAI + speed <= winWidht:
                    xAI += speed
                    numberOfMoves += 1
            if posMove == 2:
                if yAI + speed <= winHeight:
                    yAI += speed
                    numberOfMoves += 1
            if posMove == 3:
                if xAI - speed >= 0:
                    xAI -= speed
                    numberOfMoves += 1
            if posMove == 4:
                pass

            # verify if opponent cross the downLimit
            for i in range(0, len(opponents)):
                if opponents[i][1] > winHeight:
                    opponents[i][1] = random.randint(1, winMiddleLimit)
                    opponents[i][0] = random.randint(1, winWidht)

            # verify if AI crash
            for i in range(0, len(opponents)):
                oppC = opponents[i]
                if oppC[0] < xAI or oppC[0] > xAI+dimension:
                    continue
                if oppC[1] < yAI or oppC[1] > yAI+dimension:
                    continue

                crash = True
            t+=1
            if t == 10000:
                crash = True

        print(t," ", numberOfMoves," ", t/numberOfMoves)
        self.__time = t
        self.__fitness = t / numberOfMoves

