import numpy as np
from tqdm import trange, tqdm
stones = np.loadtxt('Inputs/day11Input.txt', delimiter=' ', dtype=int)
# stones = np.array([stones])

track={} # Store eventual progress

def RuleOne(x): 
    '''x is 0 --> return [1]'''
    return [1]

def RuleTwo(x):
    '''x has even # digits --> split digits in two'''
    half = len(str(x))//2
    return [int(str(x)[:half]), int(str(x)[half:])]

def RuleThree(x):
    '''x * 2048'''
    return [np.int64(x)*2048]
    
def Operate(stones):
    '''Performs the changes on the stone list as an array'''
    # Find only unique values
    uniStones, counts = np.unique(stones, return_counts=True)
    
    # Find indices for the rules in order 
    idxFirst = uniStones==0
    idxSecond = (np.floor(np.log10(uniStones))%2==1)&(~idxFirst)
    idxThird = (~idxFirst)&(~idxSecond)

    # act on rules
    if counts[idxFirst].size>0:
        newstones = [1]*counts[idxFirst][0] # add zeros
    else: newstones=[]
    
    # split numbers with even # digits
    tmp = []
    for i, count in tqdm(zip(uniStones[idxSecond].astype(str), counts[idxSecond]), leave=False):
        tmp.extend([int(i[:len(i)//2]), int(i[len(i)//2:])]*count)
    newstones.extend(tmp)

    # Third option is to multiply
    for i, count in tqdm(zip(uniStones[idxThird], counts[idxThird]), leave=False): newstones.extend([np.int64(i)*2048]*count)
    
    return np.array(newstones, dtype='int64')

# def Operate(stone):
#     '''New method to operate'''
#     if stone==0: out = RuleThree(stone)
#     elif np.floor(np.log10(stone))%2: out = RuleTwo(stone)
#     else: out = RuleThree(stone)

#     return out


for i in range(25):
    stones=Operate(stones)



# hold=[]
# for i in range(25):
#     for j in stones:
        
#             hold.Operate(stones)
#         print(stones.size)
print(f'After 25 runs we have {stones.size} stones')
input()


################### 
###### PART B
###################



for i in trange(75-25):
    stones = Operate(stones) 

print(f'After 25 runs we have {stones.size} stones')
