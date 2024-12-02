import numpy as np


# Track how many safe rows
safe=0
with open('Inputs/day2Input.txt') as f:
    for line in f.readlines():
        # Remove the string formatting and set into an array of ints
        row = np.asarray(line.strip().split(' '), dtype='int')
        
        # Find the running difference
        diff = np.diff(row)

        if ((all(diff<0))|(all(diff>0)))&(all(abs(diff)<=3)): safe+=1

print(f'Found {safe} safe rows')


##################################
### Part2 #####
##################################
# Uses the same input as the first part

runTest = lambda diff : ((all(diff<0))|(all(diff>0)))&(all(abs(diff)<=3))

# Track how many safe rows
safe=0
with open('Inputs/day2Input.txt') as f:
    for line in f.readlines():
        # Remove the string formatting and set into an array of ints
        row = np.asarray(line.strip().split(' '), dtype='int')
        
        # Find the running difference
        diff = np.diff(row)

        # No incorrect levels
        if runTest(diff): safe+=1

        # if any incorrect levels, iteratively remove elements and test
        else: 
            for i in range(row.size): 
                tmp = np.delete(row, i)
                tmpdiff = np.diff(tmp)
                if runTest(tmpdiff): 
                    safe+=1
                    break

print(f'Found {safe} safe rows')