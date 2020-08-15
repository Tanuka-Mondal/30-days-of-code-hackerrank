#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
   
    num = int(input())

    ans = 0
    maxnum = 0

while num > 0:
    if num % 2 == 1:
        ans += 1
        if ans > maxnum:
            maxnum = ans

    else:
        ans = 0

    num //= 2

print(maxnum)
