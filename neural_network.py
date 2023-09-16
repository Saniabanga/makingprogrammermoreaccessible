"""
Created on September 17th

@author: David Gayowsky

Simple neural network using PyTorch to process signal data: classification algorithm.
"""

#######################################################################

import numpy as np
import math 
import torch
import matplotlib.pyplot as plt
import copy
import os
import torch.optim as optim
import torch.nn as nn
from torch.nn import Linear, ReLU, Sigmoid, Module, BCELoss, Softmax
from torch import Tensor
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import itertools
from torch.utils.data import Dataset, TensorDataset, DataLoader
from torch.utils.data.dataset import random_split

#device = 'cuda' if torch.cuda.is_available() else 'cpu'
#DONT USE CUDA UNLESS YOU'RE ME (DAVID)
device = 'cpu'

#######################################################################

'''Args:
p: number of sensor inputs
input_data_array: any given array of data
all_sensor_data: position data from glove sensors of size P, where for all p in p, len(p) >=  1
all_recorded_outputs: outputs corresponding to each point of position data of size P
all_possible_outputs: all possible outputs, e.g. for all p in P, p in all_possible_outputs
y: number of possible outputs'''

p = 24
y = 9

#######################################################################

#Define a function to receive data from file.
def extract_data():
     return 

#Define a function to convert our data into a tensor.
#Note that we can use this to convert any array into a tensor.

def convert_data(input_data_array):

    #Basically we just throw this in a pytorch tensor.
    data_tensor = torch.tensor(input_data_array)
                                
    return data_tensor

#Define a function to split data into training and testing data.
#We don't necessarily need this, but it's nice to have! 
def training_testing_data(all_sensor_data, all_recorded_outputs, all_possible_outputs):
     
    #Create index IDs and shuffle them, then grab half of them to be training data.
    index_ids = np.arange(len(all_recorded_outputs))
    np.random.shuffle(index_ids)
    train_indices = index_ids[:math.floor(0.5*len(all_sensor_data))]
    training_data = all_sensor_data[train_indices]

    #... ad nauseum, I won't finish this function for now because we don't really need 
    #this for the purposes of this hackathon.

#######################################################################

#Actual neural network code:

#Create class for our NN:
class NeuralNetwork(nn.Module):
    
    #Define neural network structure with init:
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer_1 = nn.Linear(p, 16+p) 
        self.activation_1 = nn.ReLU()
        self.layer_2 = nn.Linear(16+p, 32+p) 
        self.activation_2 = nn.ReLU()
        self.layer_out = nn.Linear(32+p, y)
        self.activation_out = nn.Tanh()

    #Define forward pass across layers with functions:
    def forward(self, inputs):
        x = self.activation_1(self.layer_1(inputs))
        x = self.activation_2(self.layer_2(x))
        x = self.activation_out(self.layer_out(x))
        return x