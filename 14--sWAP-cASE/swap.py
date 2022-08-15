def swap_case(s):
    i = 0
    new_string = ""
    if(len(s) <= 1000 and len(s) > 0):
        while i < len(s):
            if(s[i].isalpha()):
                if(s[i].islower()):
                    new_string += s[i].upper()
                elif(s[i].isupper()):
                    new_string += s[i].lower()
                else:
                    new_string += s[i]
            else:
                new_string += s[i]
            i+=1
        return new_string