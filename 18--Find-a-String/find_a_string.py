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