
from Matrix import Matrix
import numpy as np

def sigmoid(x):
    return .5 * (1 + np.tanh(.5 * x))

class NeuralNetwork():
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.__inputNodes = input_nodes
        self.__hiddenNodes = hidden_nodes
        self.__outputNodes = output_nodes
        
        self.__weightsIH = Matrix(self.__hiddenNodes, self.__inputNodes)
        self.__weightsHO = Matrix(self.__outputNodes, self.__hiddenNodes)

        self.__biasH = Matrix(self.__hiddenNodes, 1)
        self.__biasO = Matrix(self.__outputNodes, 1)

        self.__weightsIH.randomize()
        self.__weightsHO.randomize()
        self.__biasH.randomize()
        self.__biasO.randomize()
    
    def getDimensionWeightsIH(self):
        return [self.__hiddenNodes, self.__inputNodes]
    def getDimensionWeightsHO(self):
        return [self.__outputNodes, self.__hiddenNodes]


    def getWeightsIHPos(self, posI, posJ):
        return self.__weightsIH.getDataPos(posI, posJ)
    def getWeightsHOPos(self, posI, posJ):
        return self.__weightsHO.getDataPos(posI, posJ)

    def setWeightIHPos(self, posI, posJ, val):
        self.__weightsIH.setDataPos(posI, posJ, val)
    def setWeightHOPos(self, posI, posJ, val):
        self.__weightsHO.setDataPos(posI, posJ, val)


    def feedForward(self, inputArray):
        # generating te Hidden Outputs
        inputs = Matrix.fromArray(inputArray)
        
        hidden = Matrix.multiply(self.__weightsIH, inputs)
        hidden.add(self.__biasH)
        hidden.map(sigmoid)

        # generating te outputs
        output = Matrix.multiply(self.__weightsHO, hidden)
        output.add(self.__biasO)
        output.map(sigmoid)
        # sending back
        return output.toArray()

