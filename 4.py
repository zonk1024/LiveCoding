#!/usr/bin/env python

cur_max = 0

def is_palindromic(v):
    v = str(v)
    for i in range(len(v)/2):
        if v[i] != v[len(v) - i - 1]:
            return False
    return True

for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        value = i * j
        is_p = is_palindromic(value)
        if is_p and value > cur_max:
            print i, j, value
            cur_max = value

print cur_max
