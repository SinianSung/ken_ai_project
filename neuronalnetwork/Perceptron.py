import random

class Perceptron:
    """
        Simple Perceptronclass with constructor
        perceptron(number of inputs, learningrate)
    """
    num_input_nodes =0
    bias = 0
    weights = []
    count=0
    plus=0
    minus=0

    learning_rate = 0.002

    def __init__(self, num, learning_rate):
        """
            Konstructor of the class
        """
        self.num_input_nodes = num
        for i in range(num):
            self.weights.append(random.random()*2-1)
        self.learning_rate = learning_rate
        
    def guess(self, inputs):
        """
            returns the value/guess of the perceptron for the
            given inputs
        """
        if len(inputs)!= self.num_input_nodes:
            return 
        sum = 0
        for i in range(len(inputs)):        
            sum += inputs[i]* self.weights[i]
        return self.activate(sum)

    def train(self, inputs, desired):
        """
            trainigmethod, inputs processed and compared to desired result
            adjustment of weights by Error * learningconstant
        """
        guessvalue = self.guess(inputs)
        error = desired - guessvalue
        if error ==0:
            self.plus+=1
        else:
            self.minus +=1
        # weight-correction
        for i in range(len(inputs)):
            self.weights[i]  += self.learning_rate*error*inputs[i]

    def activate(self, sum):
        """
            Activationfunktion returns 1 if the weighted sum of the
            given inputs are positive
        """
        if sum>0:
            return 1
        else:
            return -1

    def getWeights(self):
        """
            return weights
        """
        return self.weights


