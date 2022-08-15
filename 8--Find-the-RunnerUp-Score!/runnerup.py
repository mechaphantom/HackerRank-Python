if __name__ == '__main__':
    n = int(input())
    if(n <= 10 and n >= 2):
        list1 = [None] * n
        list1 = list(map(int, input().split()))
        list2 = list(set(list1))
        list2.sort()
        print(list2[-2])

# Another possible solution
"""
def findSM(l):
    f, s = l[0], l[0]
    for i in range(len(l)):
        if l[i] > f:
            s, f = f, l[i]
        elif l[i] < f:
            if f == s:
                s = l[i]
            elif l[i] > s:
                s = l[i]
    return s            

n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])

print(findSM(l))
"""