import numpy

class neuronalNetwork:

    #initialise the neuronal Network
    def __init__(self, inputnodes, hiddennotes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))


        #learning rate
        self.lr = learningrate

        self.activation_function = lambda x: scipy.special.expit(x)


    #train the neuronal Network
    def train():
        pass

    # query the neuronal Network
    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndim-2).the

        hidden_inputs = numpy.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs
    