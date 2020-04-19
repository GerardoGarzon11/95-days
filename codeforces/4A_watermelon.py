#!/usr/bin/env pypy

w = int(input())

print("YES" if w % 2 == 0 and w > 2 else "NO", end="")
