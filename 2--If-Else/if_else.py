#Solution Way #1 for Python3
n = int(input())
if (n <= 100 and n >= 1):
    if (n % 2 != 0):
        print("Weird")
    if (n % 2 == 0):
        if (n <= 5 and n >= 2):
            print("Not Weird")
        if (n <= 20 and n >= 6):
            print("Weird")
        if (n > 20):
            print("Not Weird")

#Solution Way #2 for Python2
"""
import sys
n = int(raw_input().strip())
if n%2==1:
    print "Weird"    
elif n%2 == 0 and 2 <= n <= 5:
    print "Not Weird"
elif n%2 == 0 and 6 <= n <= 20:
    print "Weird"
else:
    print "Not Weird"
"""