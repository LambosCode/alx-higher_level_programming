#!/usr/bin/python3
def element_at(my_list, idx):
    if len(my_list) == 0:
        return None
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
