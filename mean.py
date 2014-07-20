

import sys

sum = 0
n = 0
#sum input values
for num in open('data.txt'):
    sum += float(num)
    n += 1

print sum / n

#print the mean of the numbers givin in a file
