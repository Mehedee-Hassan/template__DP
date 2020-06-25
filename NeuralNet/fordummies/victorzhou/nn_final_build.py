# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:13:11 2020

@author: mehedee

final basic NN template

"""



import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))


def deriv_sigmoid(x):
    
    fx = sigmoid(x)
    return fx * (1-fx)


def mse_loss(y_true,y_pred):
    return ((y_true - y _pred)**2).mean()

class NeuralNet:
    
    def __init__(self):
        
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        
        # Biases
        
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
        
        
    def feedForward(self,x):
        
        
        h1 = sigmoid(self.w1 * x[0]+self.w2 * x[1]+self.b1)
        h2 = sigmoid(self.w3 * x[0]+self.w4 * x[1]+self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        
        return o1
    
    def train(self,data,all_y_trues):
        learn_rate  = 0.1
        epochs = 1000
        
        for epoch in range (epochs):
            for x,y_true in zip(data,all_y_trues):
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sgmoid(sum_h1)
                                
                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)
                
                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)                               


                y_pred = o1
                
                # calculate partital derivatives
                # nameing d_L_d_w1 represents Partial L/partial w1
                
                
                d_L_d_ypred = -2 * (y_true - y_pred)
                
                
                # Neuron  o1
                
                d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)


                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1) 
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)
                
                
                # neuron h1 
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h2)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)
                
                
                # neuron h2
                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                
                
                
                



