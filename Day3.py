import re

score=0
with open('Inputs/day3Input.txt') as f:
    s = f.read()
    # Extract the mul(d,d) patterns
    ext = re.findall('mul\(\d*,\d*\)', s)
    # break down to pairs
    pairs = [i.strip('mul()').split(',') for i in ext]

    # Multiple and add to score
    for i in pairs:score+=int(i[0]) * int(i[1])


print(f'Final score : {int(score)}')

score=0
with open('Inputs/day3Input.txt') as f:
    s = f.read()
    # Extract the mul(d,d) patterns and the do() don'() patterns
    ext = re.findall("mul\(\d*,\d*\)|don't\(\)|do\(\)", s)
    
    # Stores all the activated mul(d,d) functions
    newlist = []
    keep=True
    for i in ext:
        # Swtiches the activation on and off
        if i=="don't()": keep=False
        elif i=="do()": keep=True
        
        # If mul(d,d) and keep append to list
        elif keep: 
            pair = i.strip('mul()').split(',')
            score+=int(pair[0])*int(pair[1])

print(f'Final score : {int(score)}')
        
