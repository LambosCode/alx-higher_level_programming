#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        lst_v = list(a_dictionary.values())
        max_v = max(lst_v)
        for x in a_dictionary:
            if max_v == a_dictionary[x]:
                max_k = x
    return max_k
