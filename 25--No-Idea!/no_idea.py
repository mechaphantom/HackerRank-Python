a=input().split(' ')
l=([int(i) for i in input().split(' ')])
firstset=set([int(i) for i in input().split(' ')])
secondset=set([int(i) for i in input().split(' ')])
p=0
for i in l:
    if i in firstset:
        p+=1
    if i in secondset:
        p-=1
print(p)

# Another Possible Solution Way
"""
n, m = input().split()
n_int, m_int = int(n), int(m)
n_integers_for_array = input().split()
n_array = [eval(i) for i in n_integers_for_array]
m1_integers_for_set, m2_integers_for_set = input().split(), input().split()
m1, m2 = list(set(m1_integers_for_set)), list(set(m2_integers_for_set))
if(((n_int <= 10**9) and (n_int >= 1)) and ((m_int <= 10**9) and (m_int >= 1)) and (x for x in m1 if m1[x] <= 10**9 and m1[x] >= 1) and (x for x in m2 if m2[x] <= 10**9 and m2[x] >= 1)):
    if(((n_int <= 10**5) and (n_int >= 1)) and ((m_int <= 10**5) and (m_int >= 1))):
        happiness = 0
        for i in range(len(m1)):
            if(m1[i] in str(n_int)):
                happiness += 1
                print("+ ", happiness)
            if(m2[i] in str(n_int)):
                happiness -= 1
                print("- ", happiness)
        print(happiness)
"""