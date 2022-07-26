import matplotlib.pyplot as plt
import numpy as np
import math

def tanh(x):
    tanh = ((np.exp((2*x)) - 1) / ((np.exp(2*x)) + 1))
    return print("TanH value at "+ str(x) + " is",tanh)

def tan_derivative(x):
    tan_der = 1-(((np.exp((2*x)) - 1) / ((np.exp(2*x)) + 1)))**2
    return print("TanH slope at "+ str(x) + " is {:.2f}".format(tan_der))

tan_derivative(10)
tanh(0)