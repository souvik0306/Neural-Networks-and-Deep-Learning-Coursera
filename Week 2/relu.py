import matplotlib.pyplot as plt
import numpy as np
import math

def relu(x):
    g = max(0,x)
    return print(g)

def leaky(x):
    g = max(0.01*x,x)
    return print(g)

relu(-1)
leaky(0)
