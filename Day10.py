import numpy as np
from time import time

mapp = []
with open('Tests/day10Input.txt') as f:
    for line in f.readlines():
        mapp.append(list(line.strip()))
mapp = np.asarray(mapp).astype(int)

starttime=time()

print(mapp)
print()

# Find starting points
allstart = np.where(mapp==0)

def LookAhead(coords, mapp=mapp):
    '''Looks in all four directions to search for correct step if it exists'''
    if type(coords)==tuple:
        # Only one coordinate
        y,x=coords

        # Send 4 walkers for each direction from initial coord
        # Ensure it doesn' go out of bounds
        walker_y = np.array([min(y+1,mapp.shape[0]-1), max(y-1,0), y, y ])
        walker_x = np.array([x, x, min(x+1,mapp.shape[1]-1), max(x-1,0)])

        # Compare possible values
        currentVal = mapp[y,x]
        possVals = mapp[(walker_y, walker_x)]

        nextvals = possVals==currentVal+1
        if not any(nextvals): return # all routes are dead
        else: 
            # Check if any finish
            finish = possVals==9
            if any(finish)&(currentVal==8):
                # Don't double count same finish from different routes
                global finishCoords
                newFinish = [(y,x) for y,x in zip(walker_y[finish], walker_x[finish])]
                for fin in newFinish: 
                    if fin not in finishCoords:
                        finishCoords.append(fin)

                nextvals[finish]=False # Stop at the peak
            
            # Some next steps
            nextCoords = [(y,x) for y,x in zip(walker_y[nextvals], walker_x[nextvals])]
            
            # Track motion
            # print(f'\nCurrentPos = {coords}')
            # print(f'Nextposition = {nextCoords}\n##########')
            # input()
            return nextCoords
        
    elif type(coords)==list:
        # Multiple points to check
        state = []
        for i in coords:
            look=LookAhead(i)

            if look==None: 
                continue # Route is dead
            
            elif len(look)==0: continue # end of run

            else:
                # Can still move
                for m in look:
                    if m not in state: state.append(m)
                # if look[0] not in state:
                #     state.extend(look)

        return state
        

scores = []
for si, sj in zip(allstart[0], allstart[1]):
    print(f'Starting with coord {(si,sj)}')
    # for each possible start
    score=0 # reset score
    finishCoords = []
    alive=True

    # First look
    pos = LookAhead((si,sj))
    # print(pos)
    if pos==None: continue # Dead start
    while alive:

        pos = LookAhead(pos)
        if len(pos)==0: alive=False
    
        # print('\n###### NEXTLOOP ########\n')
    
    # print(finishCoords)
    score+=len(finishCoords)
    scores.append(score)

# print(f'all scores are {scores}')
print(f'Time taken = {time()-starttime}')
print(f'Sum of scores = {sum(scores)}')


###############################################
########## Part b ####################
print('\n\n PART B \n\n')

def LookAhead(coords, mapp=mapp):
    '''Looks in all four directions to search for correct step if it exists'''
    if type(coords)==tuple:
        # Only one coordinate
        y,x=coords

        # Send 4 walkers for each direction from initial coord
        # Ensure it doesn' go out of bounds
        walker_y = np.array([min(y+1,mapp.shape[0]-1), max(y-1,0), y, y ])
        walker_x = np.array([x, x, min(x+1,mapp.shape[1]-1), max(x-1,0)])

        # Compare possible values
        currentVal = mapp[y,x]
        possVals = mapp[(walker_y, walker_x)]

        nextvals = possVals==currentVal+1
        if not any(nextvals): return # all routes are dead
        else: 
            # Check if any finish
            finish = possVals==9
            if any(finish)&(currentVal==8):
                # Don't double count same finish from different routes
                global finishCoords
                newFinish = [(y,x) for y,x in zip(walker_y[finish], walker_x[finish])]
                finishCoords.extend(newFinish)

                nextvals[finish]=False # Stop at the peak
            
            # Some next steps
            nextCoords = [(y,x) for y,x in zip(walker_y[nextvals], walker_x[nextvals])]
            
            # Track motion
            print(f'\nCurrentPos = {coords}')
            print(f'Nextposition = {nextCoords}\n##########')
            input()
            return nextCoords
        
    elif type(coords)==list:
        # Multiple points to check
        state = []
        for i in coords:
            look=LookAhead(i)

            if look==None: 
                continue # Route is dead
            
            elif len(look)==0: continue # end of run

            else:
                # Can still move
                for m in look:
                    if m not in state: state.append(m)
                # if look[0] not in state:
                #     state.extend(look)

        return state
        

scores = []
for si, sj in zip(allstart[0], allstart[1]):
    print(f'Starting with coord {(si,sj)}')
    # for each possible start
    score=0 # reset score
    finishCoords = []
    alive=True

    # First look
    pos = LookAhead((si,sj))
    print(pos)
    if pos==None: continue # Dead start
    while alive:

        pos = LookAhead(pos)
        if len(pos)==0: alive=False
    
        # print('\n###### NEXTLOOP ########\n')
    
    # print(finishCoords)
    score+=len(finishCoords)
    scores.append(score)

    print(finishCoords)
    input()
# print(f'all scores are {scores}')
print(f'Time taken = {time()-starttime}')
print(f'Sum of scores = {sum(scores)}')