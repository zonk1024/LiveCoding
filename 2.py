#!/usr/bin/env python

evens = []

def fib():
    cur, next = 1, 1
    while True:
        yield cur
        cur, next = next, cur + next

for n in fib():
    if n > 4000000:
        break
    if not n % 2:
        evens.append(n)

print sum(evens)
