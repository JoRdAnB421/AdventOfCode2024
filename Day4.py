'''
IDEAS: - run  regex search forward and backward for each line ---> captures XMAS & SAMX
       '''


import re


with open('Inputs/day4Input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# Commonly used regex pattern
pattern = re.compile('(?=(XMAS)|(SAMX))')

initlen = len(lines[0])

# How many occurances
count=0
# covers left to right occurances 
for line in lines: count+= len(pattern.findall(line))

# Transpose the data
cols = []
for j in range(initlen):
    # Loops through characters
    s=''
    for line in lines: s+=line[j]
    cols.append(s)

# Search 
for col in cols: count+= len(pattern.findall(col))

# Shift the data to make diagonal (right diagonal)
rdiag = []
for k, line in enumerate(lines):
    # loop through each line
    if k==0:
        for i in range(initlen):
            # Loop through the characters
            s=line[i]
            for j in range(k+1, initlen):
                # Shift all following lines 
                try: s+=lines[j][j-k+i]
                except:break

            if len(s)>0: rdiag.append(s)


    else:
        s=line[0]
        for j in range(k+1, initlen):
            # Shift all following lines 
            try: s+=lines[j][j-k]
            except:break
        if len(s)>0: rdiag.append(s)

# search
for rd in rdiag: count+= len(pattern.findall(rd))

# Shift the data to make diagonal (left diagonal)
newlines=[line[::-1] for line in lines]
ldiag = []
for k, line in enumerate(newlines):
    # loop through each line
    if k==0:
        for i in range(initlen):
            # Loop through the characters
            s=line[i]
            for j in range(k+1, initlen):
                # Shift all following lines 
                try: s+=newlines[j][j-k+i]
                except:break

            if len(s)>0: ldiag.append(s)


    else:
        s=line[0]
        for j in range(k+1, initlen):
            # Shift all following lines 
            try: s+=newlines[j][j-k]
            except:break
        if len(s)>0: ldiag.append(s)
# search
for ld in ldiag: count+= len(pattern.findall(ld))

print(f'Count found to be {count}')



####### Part B
'''
They are always the same distance apart so I should be able to search'''

with open('Inputs/day4Input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
oneline=''
for line in lines:oneline+=line+'1'

initlen=len(lines[0])

print(oneline)
# regex pattern
sml=initlen-1; lrg=initlen-1
pattern = re.compile(r'(?=(M[^1]S.{{{lrg}}}A.{{{lrg}}}M.S)|(S[^1]M.{{{lrg}}}A.{{{lrg}}}S.M)|(S[^1]S.{{{lrg}}}A.{{{lrg}}}M.M)|(M[^1]M.{{{lrg}}}A.{{{lrg}}}S.S))'.format(lrg=lrg))
count = len(pattern.findall(oneline))

print(f'count found as {count}')