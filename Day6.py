import numpy as np
from tqdm import tqdm 

# Loading
mapp = []
with open('Tests/day6Input.txt') as f:
    for line in f.readlines():
        mapp.append(list(line.strip()))
mapp = np.asarray(mapp)

# start coords & obstacle position
start = np.where(mapp=='^')
obst = mapp=='#'

directions = ['N','E','S','W']

def Step(pos, dir, obst=obst):
    '''Takes steps in given direction'''
    if   dir=='N': step=[-1,0]
    elif dir=='E': step=[0,1]
    elif dir=='S': step=[1,0]
    elif dir=='W': step=[0,-1]
    
    # Potential new position, check for obstacles
    newPos = pos+step
    try:
        if not obst[newPos[0]][newPos[1]]: return True, newPos
        else: return False, pos
    except IndexError:
        return 

# Cantor pairing
Pair = lambda pos: int((pos[0]+pos[1]+1)*(pos[0]+pos[1])/2 +pos[1])
pos=np.array([i for i in start]).flatten(); point=0

# Store the id of the steps
uniquesteps=[Pair(pos)]
allSteps = [(Pair(pos), point)]

uniquesteps=[[pos[0], pos[1]]]

trapped=True
while trapped:
    # try to take a step
    step = Step(pos, directions[point])
    if step!=None:
        pos = step[1]

        if step[0]: 
            # Free space
            id = Pair(step[1])
            if [step[1][0], step[1][1]] not in uniquesteps: uniquesteps.append([step[1][0], step[1][1]])
        else: 
            # Obstacle
            point = (point + 1)%4 # Rotate right    
 
        # Track the path and direction
        allSteps.append((id, point))

    else: trapped=False
print(f'Length of unique positions = {len(uniquesteps)}') 


############ PART 2

# start coords & obstacle position
start = np.where(mapp=='^')
obst = mapp=='#'

# First find the actualy path -- no obstructions
pos=np.array([i for i in start]).flatten(); point=0

# Store the id of the steps
uniquesteps=[Pair(pos)]
allSteps = [(Pair(pos), point)]
coords = []; ids = []


trapped=True
while trapped:
    # try to take a step
    step = Step(pos, directions[point])
    if step!=None:
        pos = step[1]

        if step[0]: 
            # Free space
            id = Pair(step[1])
            if id not in uniquesteps: 
                uniquesteps.append(id)
                coords.append([i for i in step[1]])
        else: 
            # Obstacle
            point = (point + 1)%4 # Rotate right    
 
        # Track the path and direction
        allSteps.append((id, point))

    else: trapped=False


def CheckRun(obst):
    '''Checks path following new obstacle'''
    pos=np.array([i for i in start]).flatten(); point=0
    # Store current steps
    allSteps = [Pair(Pair(pos[0], pos[1]), point)]

    trapped=True
    looped=False
    while trapped:
        # try to take a step
        step = Step(pos, directions[point], obst=obst)

        if step!=None:
            pos = step[1]
            id = Pair(pos)
            if not step[0]: 
                # Obstacle
                point = (point + 1)%4 # Rotate right    
    
            # Track the path and direction
            currentStep = Pair(Pair(pos[0], pos[1]),point)
            if currentStep in allSteps[1:]: 
                trapped=False
                print(currentStep, allSteps)
                looped=True

            allSteps.append(currentStep)
        else: trapped=False
    
    if looped: return 1 
    else: return 0

numOfLoops=0
for new in coords:
    # Make a copy of map to add the new obstacle into
    newMapp = mapp.copy()

    # Add new obstacle
    newMapp[new[0],new[1]] = '#'
    newobst = newMapp=='#'
    val = CheckRun(obst=newobst)
    if val:
        print(val)
        print(newMapp)
        numOfLoops+=val 
        print()
        input()
print(f'Number of loops found = {numOfLoops}')
