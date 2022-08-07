if __name__ == '__main__':
    n = int(input())
    if(n <= 10 and n >= 2):
        list1 = [None] * n
        list1 = list(map(int, input().split()))
        list2 = list(set(list1))
        list2.sort()
        print(list2[-2])