import os
from string import digits

input = 'test.txt'
n = 1
sum = 0

with open(input) as f:
    for line in f:
        output = ''.join(c for c in line if c.isdigit())
        if len(output) > 2:
            e = len(output) - 1
            output = str(output[0]) + str(output[e])
        elif len(output) == 1:
            output = str(output) + str(output)
        else:
            pass
        print(line)    
        print(output)
        sum = sum + int(output)
        
        print(sum)
        n += 1
