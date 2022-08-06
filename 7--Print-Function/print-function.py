n = int(input())
i = 1
if(n <= 150 and n >= 1):
    while(i <= n):
        print(i, sep='', end='')
        i += 1

#Solution Way #2 for Python2
"""
from __future__ import print_function
print(*[i for i in range(1, int(raw_input())+1)], sep='')
"""