'''
IDEAS: - run  regex search forward and backward for each line ---> captures XMAS & SAMX
       '''


import re
from time import time

with open('Inputs/day4Input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

stime=time()
oneline=''
for line in lines:oneline+=line+'1'
initlen=len(lines[0])
mid=initlen
sml=initlen-1-1
smlprime=sml+1
lrg=initlen+1-1

# Regex patterns for all directions
leftright = re.compile(r'(?=(XMAS)|(SAMX))')
updown = re.compile(r'(?=(X.{{{initlen}}}M.{{{initlen}}}A.{{{initlen}}}S)|(S.{{{initlen}}}A.{{{initlen}}}M.{{{initlen}}}X))'.format(initlen=mid))
rdiag = re.compile(r'(?=([^1]X.{{{sml}}}[^1]M.{{{sml}}}[^1]A.{{{initlen}}}S)|([^1]S.{{{sml}}}[^1]A.{{{sml}}}[^1]M.{{{initlen}}}X))'.format(sml=sml, initlen=smlprime))
ldiag = re.compile(r'(?=(X[^1].{{{lrg}}}M[^1].{{{lrg}}}A[^1].{{{lrg}}}S)|(S[^1].{{{lrg}}}A[^1].{{{lrg}}}M[^1].{{{lrg}}}X))'.format(lrg=lrg))


count = len(leftright.findall(oneline)) + len(updown.findall(oneline)) + len(rdiag.findall(oneline)) + len(ldiag.findall(oneline))
totTime = time()-stime
print(f'Count found to be {count} in {totTime:.3f} s')
####### Part B
'''
They are always the same distance apart so I should be able to search'''

with open('Inputs/day4Input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

stime=time()
oneline=''
for line in lines:oneline+=line+'1'

initlen=len(lines[0])

# regex pattern
lrg=initlen-1
pattern = re.compile(r'(?=(M[^1]S.{{{lrg}}}A.{{{lrg}}}M.S)|(S[^1]M.{{{lrg}}}A.{{{lrg}}}S.M)|(S[^1]S.{{{lrg}}}A.{{{lrg}}}M.M)|(M[^1]M.{{{lrg}}}A.{{{lrg}}}S.S))'.format(lrg=lrg))
count = len(pattern.findall(oneline))

totTime = time()-stime
print(f'Count found to be {count} in {totTime:.3f} s')
