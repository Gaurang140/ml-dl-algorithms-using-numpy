from src.utils.utils import Activation
import numpy as np

# Assuming Activation class has a static method relu
x = [-1, 2, 3, 4, 5, -1000, -2, -3, -4]

# Applying ReLU activation
relu_output = Activation.relu(x)

print(relu_output)
