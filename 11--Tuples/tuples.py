if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

#Another possible solution for Python 3
"""
N = int(input())
T = tuple(int(x) for x in input().split())
print(hash(T))
"""