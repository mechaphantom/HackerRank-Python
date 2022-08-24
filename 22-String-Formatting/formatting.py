if __name__ == '__main__':
    n = int(input())
    lb = len(bin(n)) - 1
    for i in range(1,n+1):
        print('{{0: >{}}}'.format(lb-1).format(i) + '{{0: >{}}}'.format(lb).format(oct(i)[2:]) 
              + '{{0: >{}}}'.format(lb).format(hex(i)[2:].upper()) + '{{0: >{}}}'.format(lb).format(bin(i)[2:]))