import os
def solve(s):
    if(len(s) < 1000 and len(s) > 0):
        for i in s.split():
            s = s.replace(i,i.capitalize())
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()