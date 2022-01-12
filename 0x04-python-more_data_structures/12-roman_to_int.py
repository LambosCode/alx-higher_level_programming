#!/usr/bin/python3
def roman_to_int(roman_string):
    numb_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num_a = roman_string
    num, cnt = 0, 1
    for x in num_a:
        if cnt <= len(num_a):
            if cnt == len(num_a):
                cnt -= 1
            if numb_dict[x] >= numb_dict[num_a[cnt]]:
                    #and numb_dict[num_a[cnt]] >= numb_dict[num_a[cnt+1]]:
                cnt += 1
                num += numb_dict[x]
            else:
                num -= numb_dict[x]
    return num
