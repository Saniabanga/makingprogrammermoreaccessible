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

#######################################################################