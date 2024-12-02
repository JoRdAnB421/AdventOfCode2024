import numpy as np


# Load the data 
safe=0
with open('Inputs/day2Input.txt') as f:
    for line in f.readlines():
        # Remove the string formatting and set into an array
        row = np.asarray(line.strip().split(' '), dtype='int')
        
        diff = np.diff(row)

