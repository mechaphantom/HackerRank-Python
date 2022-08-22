def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        comparison_string = ""
        comparison_string += string[i:len(sub_string)+i]
        if(comparison_string == sub_string):
            count += 1
        i += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


#Another possible solution way

"""
big_str = input()
small_str = input()
small_len = len(small_str)
count = 0

for i in range(len(big_str[:-small_len + 1])):
    if(big_str[i:i+small_len] == small_str):
        count += 1

print(count)
"""