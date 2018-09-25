#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())
if n%2==0:
    if 2<=n<=5 or n>20:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print('Out of Range')
elif n%2==1:
    print("Weird")
else:
    print("Out of Range")
            
