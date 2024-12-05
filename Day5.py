
rules = {}
updates=[]
with open('Inputs/day5Input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line=='': continue
        elif '|' in line: 
            vals = line.split('|')
            try: rules[vals[0]].append(vals[1])
            except KeyError: rules[vals[0]] = [vals[1]]

        else:
            tmp = line
            updates.append(line.split(','))

def IsCorrect(line, rules=rules):
    '''Checks if a line obeys the rules'''
    for i, elm in enumerate(line):
        # Find if any elments have updated rules
        if elm in rules.keys():
            # Find the updated rules
            for upVal in rules[elm]:
                try: upArg = line.index(upVal)
                except ValueError:
                    continue
                # If order different to rules
                if upArg<i: return 0

    # If all rules apply then return 1     
    return 1

correct = 0
middle = 0
for line in updates:
    # Check line by line
    yes = IsCorrect(line)
    if yes:
        correct += IsCorrect(line)
        middle += int(line[len(line)//2])
        if len(line)%2==0: print(line)
        
print(f'Number of correct lines = {correct}')
print(f'Sum of middle numbers = {middle}')


##### Question 2

def IsCorrect(line, rules=rules):
    '''Checks if a line obeys the rules'''
    for i, elm in enumerate(line):
        # Find if any elments have updated rules
        if elm in rules.keys():
            # Find the updated rules
            for upVal in rules[elm]:
                try: upArg = line.index(upVal)
                except ValueError:
                    continue
                # If order different to rules
                if upArg<i: return 0, [upArg, i]

    # If all rules apply then return 1     
    return 1, None

incorrect=0
middle=0
for line in updates:
    sorted=False
    yes,arg = IsCorrect(line)

    if yes: continue 
    else:
        incorrect+=1
        while not sorted:
            # Check line by line
            if yes: 
                sorted=True
                middle += int(line[len(line)//2])
                
            else:
                # not sorted
                val = line.pop(arg[0])
                line.insert(arg[1], val)

            # Recheck  
            yes,arg = IsCorrect(line)



print(f'Number of correct lines = {incorrect}')
print(f'Sum of middle numbers = {middle}')