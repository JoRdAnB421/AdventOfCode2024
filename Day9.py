from time import time
from operator import itemgetter
from itertools import groupby
import numpy as np

with open('Inputs/day9Input.txt') as f:
    raw = f.read().strip()

starttime=time()
# Num of data blocks
numBlocks = (len(raw)-1)/2

extract = []
block=0 # Tracks the block number
for i, num in enumerate(raw):
    if not i%2:
        tmp = [block for i in range(int(num))]
        extract.extend(tmp)
        block+=1
    else:
        extract.extend(list('.'*int(num)))

extract = np.asarray(extract)

# Find location of spaces and vals to fill them
validx = np.where(extract!='.')
vals = extract[validx]

# Only spaces to be filled will be the gaps before the total length of the values
spaceidx = np.where((extract=='.')&(np.arange(0,extract.size,1)<vals.size))

# Stationary index
stillidx = (validx[0][validx[0]<vals.size],)
vals2stay = extract[stillidx].astype(int)

# moving index
mvindx = (validx[0][validx[0]>=vals.size],)
vals2Move = extract[mvindx].astype(int)

checksum = (vals2stay*stillidx[0]).sum() + (vals2Move[::-1]*spaceidx[0]).sum() # sum(val*index) after shifting


print(f'checksum = {checksum}')
print(f'Time taken = {time()-starttime}')

############################
## Part b

spaceidx = np.where(extract=='.')
st = time()
ranges=[]
for k,g in groupby(enumerate(spaceidx[0]), lambda x:x[0]-x[1]):
    # find groups of consecutive gaps or single gaps
    group = (map(itemgetter(1), g))
    group=list(map(int, group))
    # ranges.append(np.arange(group[0], group[-1]+1, 1))
    ranges.append([group[0], len(group)])
ranges=np.asarray(ranges)

# Find the unique values and how many 
univals, indices, counts = np.unique(extract, return_counts=True, return_index=True) 
comb = np.vstack((univals, indices, counts)).T # combine
comb = comb[univals!='.'].astype(int)
comb = comb[np.argsort(comb[:,0])][::-1] # sorts in decreasing order


newList = comb[-1] # First block doesn't move

for i in comb[:-1]:
    # Starting from the back check if there is space to move, 
    # if not skip but keep place
    anyGap = np.where(ranges[:,1]>=i[2])
    if anyGap[0].size==0:
        # If no space to move then continue
        newList = np.vstack((newList, i))
        continue
    # Find the first gap that can fit 
    firstFit = ranges[anyGap][0]

    if firstFit[0]>i[1]:
        # Don't move file block to the right
        newList = np.vstack((newList, i))

        continue

    # Shifts the start of the group to the gap
    i[1] = firstFit[0]
    newList = np.vstack((newList, i))
    
    # If fills gap, delete option
    if i[2]==firstFit[1]: ranges = np.delete(ranges, anyGap[0][0], axis=0) 
    else: 
        # If not filled, reduce size of gap
        new = [ranges[anyGap][0][0]+i[2], ranges[anyGap][0][1]-i[2]]
        ranges[anyGap[0][0]] = new

# Sort in order of the index
newList = newList[np.argsort(newList[:,1])]

# compute the checksum
x = newList[:,0]; i = newList[:,1]; N = newList[:,2]
checksum = x*N*(i+1/2*(N-1))

print(f'Checksum = {int(checksum.sum())}')
print(f'Time taken = {time()-st}')