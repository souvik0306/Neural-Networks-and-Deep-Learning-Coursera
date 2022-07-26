import numpy as np
import math

def sigmoid_derivative(z):
    sgm = 1/(1+np.exp(-z))
    return (sgm*(1-sgm))

print("{:.2f}".format(sigmoid_derivative(0)))