s = 'azcbobobegghakl'
currentString = s[0]
longString = currentString

for position in range(1, len(s)):
    if s[position] >= s[position - 1]:
        currentString += s[position]
    else:
        if len(currentString) > len(longString):
            longString = currentString
        currentString = s[position] 

if len(currentString) == len(s):
    longString = currentString

print('Longest substring in alphabetical order is: ' + longString)

