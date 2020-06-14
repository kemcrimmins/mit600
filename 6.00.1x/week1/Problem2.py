s = 'azcbobobegghakl'
numBobs = 0

for position in range(len(s)-2):
    if s[position] == 'b' and s[position:position+3] == 'bob':
        numBobs += 1

print('Number of times bob occurs is: ' + str(numBobs))

