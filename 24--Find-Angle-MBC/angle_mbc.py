import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)
ab = int(input())
bc = int(input())
hypo = math.sqrt((ab*ab)+(bc*bc))
value = bc/hypo
result = math.acos(value)
print(str(normal_round(math.degrees(result))) + '\u00B0')