import random


# Class Matrix contain number of rows, number of columns, data of matrix and operation with matrix
class Matrix():

    # Desc:
    # In:
    # Out:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__data = []

        for i in range(0, self.__rows):
            self.__data.append([])
            for j in range(0, self.__cols):
                self.__data[i].append(0)

    def getRows(self):
        return self.__rows
    def getCols(self):
        return self.__cols

    def getData(self):
        return self.__data
    def getDataPos(self, posI, posJ):
        return self.__data[posI][posJ]
    def setDataPos(self, posI, posJ, val):
        self.__data[posI][posJ] = val


    # Desc:     populate data of matrix with random number
    # In:       ----
    # Out:      new data in matrix      
    def randomize(self):
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                self.__data[i][j] = random.uniform(-1,1)
    

    # Desc:     create a Matrix object from an array
    # In:       array
    # Out:      Matrix with one column
    def fromArray(arr):
        m = Matrix(len(arr), 1)
        for i in range(0, len(arr)):
            m.__data[i][0] = arr[i]
        return m

    def toArray(self):
        arr = []
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                arr.append(self.__data[i][j])
        return arr

    # Desc: create transpose of matrix
    # In:   self object
    # Out:  return transpose of current matrix
    def transpose(matrix):
        result = Matrix(matrix.__cols, matrix.__rows)

        for i in range(0, result.__rows):
            for j in range(0, result.__cols):
                result.__data[i][j]  = matrix.__data[j][i]

        return result


    # Desc:     multiply two Matrix
    # In:       two Matrix
    # Out:      return the Matrix result 
    def multiply(a, b):
        if a.getCols() != b.getRows():
            raise ValueError("columns of a != rows of b")
        else:
            result = Matrix(a.getRows(), b.getCols())
            
            for i in range(0, result.__rows):
                for j in range(0, result.__cols):
                    sum = 0
                    for k in range(0, a.__cols):
                        sum += a.__data[i][k] * b.__data[k][j]
                    result.__data[i][j] = sum
            return result
    

    # Desc:     multiply all value of matrix with a number  
    # In:       number m
    # Out:      modify current Matrix
    def multiplyValue(self, m):
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                self.__data[i][j] *= m
                

    # Desc:     add to all value of matrix a number  
    # In:       number m
    # Out:      modify current Matrix
    def add(self, m):
        if(isinstance(m, Matrix)):
            mat = m.getData()
            for i in range(0, self.__rows):
                for j in range(0, self.__cols):
                    self.__data[i][j] += mat[i][j]
        else:
            for i in range(0, self.__rows):
                for j in range(0, self.__cols):
                    self.__data[i][j] += m
    
    
    # Desc:     substract a from b  
    # In:       matrix a and b
    # Out:      substract Matrix
    def substract(a, b):
        result = Matrix(a.__rows, b.__cols)

        for i in range(0, result.__rows):
            for j in range(0, result.__cols):
                result.__data[i][j] = a.__data[i][j] - b.__data[i][j]
        return result


    # Desc:     applay a function to all elements of matrix 
    # In:       number m
    # Out:      modify current Matrix
    def map(self, fn):
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                val = self.__data[i][j]
                self.__data[i][j] = fn(val)


    # Desc:     print current Matrix
    # In:       --
    # Out:      --
    def print(self):
        print(self.__data)


