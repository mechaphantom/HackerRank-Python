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