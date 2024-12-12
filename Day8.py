import numpy as np

mapp = []

# Loading the data as a map 
with open('Inputs/day8Input.txt') as f:
    for line in f.readlines():
        mapp.append(list(line.strip()))

mapp = np.asarray(mapp)

# find unique nodes
uniqueNodes = np.unique(mapp)

# Find all instances of unique nodes
allNodes = {}
uniqueAntinodes=[]
for node in uniqueNodes:
    if node=='.': continue # Don't care for empty spaces
    where = np.where(mapp==node) # Find coordinates and arange nicely
    coords = np.vstack((where[0],where[1])).T
    allNodes[node] = coords # Save coords 

    for i, first in enumerate(coords[:-1]):
        # For each node type, compare against the other same nodes 
        dists = coords[i+1:]-first

        # Before first and after second
        bf = first-dists; aftsec = coords[i+1:]+dists

        # Only those in the map
        bf = bf[(bf[:,0]>=0)&(bf[:,0]<mapp.shape[0])&(bf[:,1]>=0)&(bf[:,1]<mapp.shape[1])]
        aftsec = aftsec[(aftsec[:,0]>=0)&(aftsec[:,0]<mapp.shape[0])&(aftsec[:,1]>=0)&(aftsec[:,1]<mapp.shape[1])]        

        # Combine all locations
        possLoc = np.vstack((bf, aftsec))


        if len(uniqueAntinodes)==0: uniqueAntinodes=possLoc
        else: uniqueAntinodes = np.vstack((uniqueAntinodes, possLoc))
    
uniqueAntinodes=np.unique(uniqueAntinodes, axis=0)
print(f'Number of unique antinodes={len(uniqueAntinodes)}')



##################################
#### PART 2
'''
IDEA : once you find two nodes you find the line that connects them and 
then every integer coordinate that sits on the line should be included
'''
print(mapp.shape)
def FindIntegerCoords(grad, coords, xrange=np.arange(0,mapp.shape[1],1)):
    '''Finds all of the integer coordinates for a given line'''
    allpos=[]
    for xval in xrange:
        yvals = coords[0]+grad*(xval-coords[1]) # Y position on line 
        idx = np.where((yvals==yvals.astype(int))&(yvals<mapp.shape[0])&(yvals>=0))
        tmp = np.vstack((yvals[idx], np.ones_like(yvals[idx])*xval)).T
        if xval==0:
            allpos=tmp
        else:
            allpos = np.vstack((allpos, tmp))
    return allpos

uniqueAntinodes=[]
for node in uniqueNodes:
    if node=='.': continue # Don't care for empty spaces
    where = np.where(mapp==node) # Find coordinates and arange nicely
    coords = np.vstack((where[0],where[1])).T
    allNodes[node] = coords # Save coords 

    for i, first in enumerate(coords[:-1]):
        # For each node type, compare against the other same nodes 
        dists = coords[i+1:]-first

        grad = dists[:,0]/dists[:,1] # Gradient of the lines connecting nodes
        possLoc = FindIntegerCoords(grad, first)

        if len(uniqueAntinodes)==0: uniqueAntinodes=possLoc
        else: uniqueAntinodes = np.vstack((uniqueAntinodes, possLoc))
    
uniqueAntinodes=np.unique(uniqueAntinodes, axis=0)

print(f'Number of unique antinodes={len(uniqueAntinodes)}')
