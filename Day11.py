import numpy as np
from tqdm import trange
stones = np.loadtxt('Inputs/day11Input.txt', delimiter=' ', dtype=int)

def Operate(stones):
    '''Performs one operation of the stones'''
    newStones=[]
    for stone in stones:
        # implement rules for change
        if stone==0:
            newStones.append(1)

        elif not len(str(stone))%2:
            tmp = [str(stone)[:int(len(str(stone))/2)], str(stone)[int(len(str(stone))/2):]]
            newStones.extend(tmp)

        else:
            newStones.append(np.int64(stone)*2024)
    newStones = np.asarray(newStones).astype('int64')
    return newStones

for i in range(25):
    stones = Operate(stones)

print(f'After 25 runs we have {stones.size} stones')


################### 
###### PART B
###################

def OperateArray(stones):
    '''Performs the changes on the stone list as an array'''
    # Find indices for the rules in order 
    idxFirst = stones==0
    idxSecond = (np.floor(np.log10(stones))%2==1)&(~idxFirst)
    idxThird = (~idxFirst)&(~idxSecond)

    # act on rules
    newstones = np.zeros(sum(idxFirst)) # add zeros

    # split numbers with even # digits
    tmp = []
    for i in stones[idxSecond].astype(str):
        tmp.extend([int(i[:len(i)//2]), int(i[len(i)//2:])])
    tmp = np.asarray(tmp, dtype='int64')
    newstones = np.append(newstones, tmp)

    # Third option is to multiply
    newstones = np.append(newstones, stones[idxThird]*2048)

    return newstones.astype('int64')

for i in trange(75-25):
    stones = OperateArray(stones) 

print(f'After 25 runs we have {stones.size} stones')
