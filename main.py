
import matplotlib.pyplot as plt
import csv
import numpy as np
import keras as kr


iris = np.array(list(csv.reader(open('iris.csv'))))[1:] #Skipping header
print(type(iris))
X=iris[:,:4]
y=iris[:,4]



