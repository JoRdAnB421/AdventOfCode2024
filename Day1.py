import numpy as np

# Load and unpack the columns
c1, c2 = np.loadtxt('Inputs/day1Input.txt', unpack=True)

# Sort both columns
c1.sort(); c2.sort()

# Find the sum of the differences
sum_diff = np.sum(abs(c1-c2))

print(f'Sum of differences is {int(sum_diff)}')



##################################################
#### Part 2 ####

# Load and unpack the columns
c1, c2 = np.loadtxt('Inputs/day1P2Input.txt', unpack=True)

# Sort first
c1.sort() ; c2.sort()

# Identify numbers that appear in c2 and c1 
c2 = c2[np.isin(c2, c1)] ; c1 = c1[np.isin(c1,c2)]

# Count up the number of times each number appears
c2Uni, counts2 = np.unique(c2, return_counts=True)
c1Uni, counts1 = np.unique(c1, return_counts=True)

# Sum of the repated numbers from c1 to c2
sum_repeats = np.sum(c1Uni*counts1*counts2)

print(f'Sum of the repeats {int(sum_repeats)}')