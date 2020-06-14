s = 'ffff'

vowels = 'aeiou'
numVowels = 0
for char in s:
    if char in vowels:
        numVowels += 1
print('Number of vowels: ' + str(numVowels))

