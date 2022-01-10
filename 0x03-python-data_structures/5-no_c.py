#!/usr/bin/python3
def no_c(my_string):
    ln = 0
    lnth = len(my_string)
    strn = ""
    while ln < lnth:
        if my_string[ln] == 'c' or my_string[ln] == 'C':
            ln = ln + 1
        else:
            strn += my_string[ln]
            ln = ln + 1
    return strn 
