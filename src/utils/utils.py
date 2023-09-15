# in this utils file you can find out the different different utils function related to algorithms for example relu and all activation function 
import numpy as np
import math

class Activation:
    def __init__(self,x):
        self.x = x
        

    @staticmethod
    def sigmoid(x):
        """
        Sigmoid activation function.

        Parameters:
            x (numpy array): Input to the sigmoid function.

        Returns:
            numpy array: Output after applying the sigmoid function element-wise.
        """
        x = np.array(x)


        pred = 1 / (1 + np.exp(-x))

        return pred
        
    

    @staticmethod
    def relu(x):
        """
       
        Relu activation function.

        Parameters:
        x (numpy array): Input to the relu function.

        Returns:
        numpy array: Output after applying the relu function element-wise.
        
    
        """
        x = np.array(x)
        x = sorted(x)
        return np.maximum(0.0,x)