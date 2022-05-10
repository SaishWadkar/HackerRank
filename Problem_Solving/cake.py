#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
candles = [3,2,1,3]
def birthdayCakeCandles(candles):
    # Write your code here
    tallest = max(candles)
    print(Counter(candles))
    print(Counter(candles).get(tallest))


birthdayCakeCandles(candles)