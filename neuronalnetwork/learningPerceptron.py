import Perceptron as pt
import random


number_of_datapoints = 20000
trainingdata = []

XMIN = -1
XMAX = 1
YMIN = -1
YMAX = 1

learning_constant = 0.01

def func(arg):
    return 0.3*arg+ 0.5

def generateData():
    """
        generates trainingdata in the form of an dictionary
        data: list of [x,y,1 ]
        output: desired value of the output
    """
    for i in range(number_of_datapoints):
        x = random.random()*(XMAX-XMIN)+XMIN
        y = random.random()*(YMAX-YMIN)+YMIN
        tag = 1
        if y <func(x):
            tag = -1
        else:
            tag = 1
        
        dataset = {'data': [x,y,1], 'output': tag}
        trainingdata.append(dataset)
    

def main():
    """
        mainfunction, creating perceptron, train, print result
    """
    #create new perceptron with 3 inputs [x,y,1] 
    ptron = pt.Perceptron(3,learning_constant)
    #generate trainigdata
    generateData()
    # print out initial weights
    print(ptron.getWeights())
    #train with generated data
    for item in trainingdata:
        ptron.train(item['data'], item['output'])
    # print out endweights
    w = ptron.getWeights()
    print(w)
    # what is the seperating line
    print(30*'=')
    print('y =',-w[0]/w[1],'x+' ,-w[2]/w[1])


if __name__ == "__main__":
    main()