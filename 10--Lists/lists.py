list = []
N = int(input())
for _ in range(N):
    operation = input() 
    if("insert" in operation):
        x = operation[7:]
        y = int(operation[9:])
        b = int(x[0].split(" ")[0])
        list.insert(b,y)
    if("append" in operation):
        x = int(operation[7:])
        list.append(x)
    if("remove" in operation):
        x = operation[7:]
        a = int(x[0])
        if(a in list):
            list.remove(a)
    if(operation == "print"):
        print(list)
    if(operation == "sort"):
        list.sort()
    if(operation == "pop"):
        list.pop()
    if(operation == "reverse"):
        list.reverse()