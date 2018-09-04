#!/usr/bin/python

import sys

def climbing_stairs(n):
  # Python program to find n-th stair  
# using step size 1 or 2 or 3.
 
# Returns count of ways to reach n-th 
# stair using 1 or 2 or 3 steps.
    if (n == 1 or n == 0) :
        return 1
    elif (n == 2) :
        return 2
     
    else :
        return climbing_stairs(n - 3) + climbing_stairs(n - 2) + climbing_stairs(n - 1) 

 
# Using dynamic programing
 
def climbing_stairs(n) :
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2
     
    for i in range(3, n + 1) :
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
     
    return res[n]
 


 
 
print(climbing_stairs(5))


if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')