from utils.utils import Activation
import numpy as np 

class Logistic_Regression(Activation):
    
    def __init__(self, x):
        super().__init__(x)
        self.sigmoid = Activation.sigmoid()