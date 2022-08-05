def is_leap(year):
    leap = False
    upper_cons = 10*10*10*10*10
    if((year <= upper_cons) and (year >= 1900)):
        if (year % 400 == 0) and (year % 100 == 0):
            leap = True
        elif (year % 4 ==0) and (year % 100 != 0):
            leap = True
        else:
            leap = False
    return leap  