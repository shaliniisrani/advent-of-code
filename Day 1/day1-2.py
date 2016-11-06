#!/usr/bin/python

f = open("input", "r")
input_str = f.read()

floor = 0 

for i,c in enumerate(input_str):
	if c == '(':
		floor += 1
	if c == ')':
		floor -= 1
        if floor == -1:
                print i, i+1
                break
