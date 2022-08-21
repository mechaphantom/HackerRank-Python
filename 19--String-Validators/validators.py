s = input()
l = list(s)
a, b, c, d, e = False, False, False, False, False
if(len(s) < 1000 and len(s) > 0):
    for x in l:
        if(x.isalnum()):
            a = True
        if(x.isalpha()):
            b = True
        if(x.isdigit()):
            c = True
        if(x.islower()):
            d = True
        if(x.isupper()):
            e = True
print(a,b,c,d,e, sep="\n")