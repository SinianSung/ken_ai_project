import csv
import math
import random as rd

import matplotlib.pyplot as plt
import numpy as np


class Datapoint:
    """
    Creates a 2-dimensional Datapoint with a tag to identify the 
    coresponding class
    """
    data = tuple()

    def __init__(self, x,y, tag):
        """
        initialises the datapoint with attributs x,y floats and a tag string
        """
        self.x = x
        self.y = y
        self.data = (x,y)
        self.tag = tag

    def __str__(self):
        return f"[({self.x}, {self.y}), {self.tag}]"

    def __repr__(self):
        return f"[({self.x}, {self.y}), {self.tag}]"
    
    def get_inputs(self):
        """
        returns the data as a list of floats
        """
        return [self.x, self.y]
    
    def get_tag(self):
        
        return self.tag

    def distance(self, other):
        """
        calculates the euclidean distance of the datapoints
        """
        abstand = (self.x-other.x)**2 + (self.y-other.y)**2 
        return math.sqrt(abstand)


class Perceptron:

    data = None
    testdata = None
    weights = list()
    learning_rate = None
    header = None
    epoch = 100
    minimum_x = None
    maximum_x = None
    fraction = 5
    

    def __init__(self, no_of_inputs, epochs, learning_rate=0.04):
        """
        no_of_inputs: number of used inputs: 2
        epochs: how many times does the system iterate the trainingsdata 
        learning_rate: what proportion of the error is used to change the weights
        """
        self.learning_rate = learning_rate
        self.epoch = epochs
        self.weights = np.zeros(no_of_inputs + 1)

    def __str__(self):
        return f"{self.learning_rate}, {self.weights}"        
           
    def predict(self, inputs):
        """
        
        """
        sum = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if sum > 0:
          activation = 1
        else:
          activation = -1            
        return activation

    def train(self):
        """
        adjust the weights with help of the trainingdata
        
        """
        for i in range(int(self.epoch)):
            if self.data == None:
                return
            for item in self.data:
                inputs = [item.x, item.y]
                label = item.tag
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * np.asarray(inputs)
                self.weights[0] += self.learning_rate * (label - prediction)

    def separator(self):
        if self.minimum_x == None or self.maximum_x == None or self.weights[1]==0:
            return
        m = -(self.weights[1]/self.weights[2])
        q = -self.weights[0]/self.weights[2]
        x= np.linspace(self.minimum_x, self.maximum_x,50)
        y =np.multiply(x,m)+q
        plt.plot(x,y, marker='.', color="black")
        
    def set_boundaries(self,x):
        if self.minimum_x == None or x<self.minimum_x:
            self.minimum_x = x
        if self.maximum_x == None or x>self.maximum_x:
            self.maximum_x = x

    def split_data(self, datalist, fraction = 6):
        """
        split data into trainingsdata and testdata
        fraction has to be at least 4.
        """
        if fraction <=3:
            fraction = 4
        self.fraction = fraction
        rd.shuffle(datalist)
        self.data , self.testdata =  datalist[:(fraction-1)*len(datalist)//fraction], datalist[(fraction-1)*len(datalist)//fraction+1:]

    def load_data(self, path, m_dict, fraction=6):
        """
        path: to the csv-file x,y,tag
        m_dict: translation of tags to matplot-markers
        """
        file = open(path,'r', newline="")
        reader = csv.reader(file)
        self.header = next(reader)
        data = []
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            self.set_boundaries(x)
            label = m_dict[row[2]]
            data.append(Datapoint(x, y, label) )
        file.close()
        self.split_data(data, self.fraction)

    def dump_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

    def __unify_data(self, data):
        all_data = {}
        if data == None:
            return
        for item in data:
            if item.tag ==1:
                tag="o"
            else:
                tag='s'
            if tag in all_data.keys():
                all_data[tag][0].append(item.x)
                all_data[tag][1].append(item.y)
            else:
                all_data[tag] = [[item.x], [item.y]]
        return all_data

    def show_data(self, istest = False):
        if istest:
            all_data = self.__unify_data(self.testdata)
        else:
            all_data = self.__unify_data(self.data)
        if all_data == None:
            return
        colors = ['purple', 'blue', 'green', 'orange']
        i = 0
        for item in all_data:
            if istest:
                plt.scatter(all_data[item][0], all_data[item][1], marker='^', c='red')
            else:
                plt.scatter(all_data[item][0], all_data[item][1], marker=item, c=colors[i])
            i += 1 

class Knn:
    """
    
    """
    k = 5
    fraction = 3
    testpoint = Datapoint(0,0,'v')
    data = None
    testdata = None
    neighbours = None
    statistics = dict()
    fig = None
    ax = None

    def __init__(self, k, fraction):
        self.k = int(k)
        self.fraction = fraction
        self.fig, self.ax = plt.subplots()

    def __str__(self):
        if self.data == None:
            return ""
        return f"knn: k={self.k}, Dataset: {len(self.data)}, Testdata: {len(self.testdata)}"
    
    def set_testpoint(self, tp):
        self.testpoint = tp

    def set_fraction(self, fraction):
        self.fraction = fraction

    def set_data(self, datalist):
        self.split_data(datalist)

    def set_testdata(self, datalist):
        self.testdata = datalist

    def get_data(self):
        if self.data == None:
            return
        out = ""
        for d in self.data:
            out += str(d)+"\n"
        return out

    def split_data(self, datalist, fraction = 6):
        rd.shuffle(datalist)
        self.fraction = fraction
        self.data , self.testdata =  datalist[:(fraction-1)*len(datalist)//fraction], datalist[(fraction-1)*len(datalist)//fraction+1:]

    def get_abstand(self,element):
        if self.testpoint == None:
            self.testpoint = Datapoint(0,0,'v')
        return self.testpoint.distance(element)

    def find_neighbors(self):
        if self.data == None:
            return
        self.data.sort(key=self.get_abstand)
        self.neighbours = self.data[:self.k]
        tags = {}
        for items in self.neighbours:
            tags[items.tag]= tags.get(items.tag,0)+1
        return max(tags, key=tags.get)

    def test(self):
        results = []
        if self.testdata == None:
            return
        for tp in self.testdata:
            self.testpoint = tp
            predicted_type = self.find_neighbors()
            results.append((tp.tag, predicted_type))
        return results

    def _unify_data(self, data):
        all_data = {}
        if data == None:
            return
        for item in data:
            if item.tag in all_data.keys():
                all_data[item.tag][0].append(item.x)
                all_data[item.tag][1].append(item.y)
            else:
                all_data[item.tag] = [[item.x], [item.y]]
        return all_data

    def show_data(self, data, istest = False):
        all_data = self._unify_data(data)
        if all_data == None:
            return
        colors = ['purple', 'blue', 'green', 'orange']
        i = 0
        for item in all_data:
            if istest:
                plt.scatter(all_data[item][0], all_data[item][1], marker='^', c='red')
            else:
                plt.scatter(all_data[item][0], all_data[item][1], marker=item, c=colors[i])
            i += 1

    def show_plot(self):
        #plt.grid(visible=True, which='both', axis='both')
        plt.show()
        
    def load_data(self, path, m_dict):
        file = open(path,'r', newline="")
        reader = csv.reader(file)
        header = next(reader)
        data = []
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            label = m_dict[row[2]]
            data.append(Datapoint(x, y, label) )
        file.close()
        self.set_data(data)

    def generate_data(self, anzahl):
        data = []
        for i in range(anzahl):
            if i % 2 == 0:
                data.append(Datapoint(rd.random(), rd.random(), "."))
            else:
                data.append(Datapoint(rd.random()+0.5,rd.random()+0.5 , "x"))
        self.set_data(data)


def main():
    
    """ p = Perceptron(2,5000, 0.05)
    p.load_data("CandyAI_red.csv", {"M&M Crispy": +1, "Skittles": -1}, 6)
    p.train()
    p.separator()
    p.show_data()
    p.show_data(istest= True)
    plt.show()
    print(p.dump_weights())"""

    model = Knn(5, 10)
    markers_dict = {'M&M': 'h', 'Skittles': '*', 'M&M Crispy': 'd'}
    model.load_data("CandyAI_red.csv",markers_dict )
    r = model.test()
    d = model.data
    t = model.testdata
    model.show_data(model.testdata, istest=True)
    model.show_data(model.data)
    model.show_plot()
    print(model)

if __name__ == "__main__":
    main()

