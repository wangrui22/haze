import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit

class NeuralNetwork(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y   

    def test(self):
        print(self.X)
        print(self.Y) 

def logistic(x):
    return 1.0/(1+np.exp(-x))

def reflect(x):
    return 1.0 - x

def main():
    # a =((1,12,"aa") , (2, 12 , "bb") , (3, 13 , "cc") , (4, 14 , "dd") )
    # print(a)
    # b = [layer[0] for layer in a]
    # print(b)
    # c= reflect
    # print(c(0.3))

    mu, sigma = 0, 0.1 # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)
    
    count, bins, ignored = plt.hist(s, 30, normed=True)
    c = 1/(sigma * np.sqrt(2 * np.pi)) 
    d = c * np.exp( - (bins - mu)2 / (2 * sigma2) )
    plt.plot(bins, c)
    plt.show()

    print(np.random.normal(0 , 1.0 , size=(10,1)))

if __name__ == "__main__":
    main()