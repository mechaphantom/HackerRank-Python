from itertools import product
integers_for_list_A, integers_for_list_B = input().split(), input().split()
list_A, list_B = [eval(i) for i in integers_for_list_A], [eval(i) for i in integers_for_list_B]
if((len(list_A) < 30 and len(list_A) > 0) and (len(list_B) < 30 and len(list_B) > 0)):
    print(*product(list_A, list_B))