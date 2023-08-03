#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        key = list(a_dictionary.keys())
        best_value = 0
        for a in range(len(key)):
            key2 = key[a]
            value = a_dictionary[key2]
            if value > best_value:
                best_value = value
                if a_dictionary[key2] == best_value:
                    best_key = key2
        return best_key
    else:
       return None
         