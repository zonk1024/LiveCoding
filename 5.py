#!/usr/bin/env python

from math import sqrt

def factor(n):
    facts = []
    n_sqrt = int(sqrt(n))
    i = 2
    while n > 1:
            if not n % i:
                facts.append(i)
                n /= i
            else:
                i += 1
    return facts

facts = {}
for i in range(2, 21):
    facts[i] = factor(i)

output = []
for values in facts.itervalues():
    for v in list(set(values)):
        v_count = values.count(v)
        o_count = output.count(v)
        if v_count > o_count:
            output.extend([v for w in range(v_count - o_count)])

final = 1
for o in output:
    final *= o
print final
