# =============================================================================
# the first perseptron/neuron
# =============================================================================

import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

class Neuron:
    def __init__(self,weights,bias):
        self.weight = weights
        self.bias = bias
        
    def feedforward(self,inputs):
        
        total = np.dot(self.weight ,inputs) +self.bias
        return sigmoid(total)
    

def testPerseptron():
    weights = np.array([0,1])
    bias = 4
    
    
    n=Neuron(weights,bias)
    x = np.array([2,3])
    
    print(n.feedforward(x))

# testPerseptron() # call me to test a single neuron

# =============================================================================
#  loss function
# =============================================================================
import numpy as np
def mseLossFunctoin(y_true,y_pred):
    return ((y_true-y_pred)**2).mean()

y_true = np.array([1,0,0,1])
y_pred = np.array([0,0,0,0])

print(mseLossFunctoin(y_true, y_pred))


# =============================================================================
# feed forward neural network
# -> the neuron
# =============================================================================

import numpy as np


class OurNeuralNetwork:
    """
    A neural network with:
        - 2 inputs
        - a hidden layer with 2 neurons (h1,h2)
        - an output layer with 1 neuron (o1)
    Each neuron has the same weights and bias:
        -w = [0,1]
        -b = 0
        
    X1---h1
      \  /\
       \/  \
       /\   o1-output
      /  \ /
     X2---h2
    """
    
    def __init__(self):
        weights = np.array([0,1])
        bias = 0
        
        self.h1 = Neuron(weights,bias)
        self.h2 = Neuron(weights,bias)
        self.o1 = Neuron(weights,bias)
    

    def feedforward(self,x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
                
        out_o1 = self.o1.feedforward(np.array([out_h1,out_h2]))
        
        return out_o1


def testNetwork():
    network = OurNeuralNetwork()
    # input to input layer
    x = np.array([2,3])
    
    print(network.feedforward(x))

    
testNetwork()


  
        




