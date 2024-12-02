import numpy as np

# Part 1
# Load and unpack the columns
data = np.loadtxt('Inputs/day1Input.txt')
c1, c2 = data[:, 0], data[:, 1]

# Compute sum of differences directly
sum_diff = np.sum(np.abs(np.sort(c1) - np.sort(c2)))

print(f'Sum of differences is {int(sum_diff)}')

##################################################
#### Part 2 ####

# Load and unpack the columns
data = np.loadtxt('Inputs/day1P2Input.txt')
c1, c2 = data[:, 0], data[:, 1]

# Sort and find common elements
common_elements = np.intersect1d(c1, c2, assume_unique=False)

# Count occurrences of each element in `c1` and `c2`
counts_c1 = np.array([np.sum(c1 == element) for element in common_elements])
counts_c2 = np.array([np.sum(c2 == element) for element in common_elements])

# Compute the sum of repeats
sum_repeats = np.sum(common_elements * counts_c1 * counts_c2)

print(f'Sum of the repeats {int(sum_repeats)}')
