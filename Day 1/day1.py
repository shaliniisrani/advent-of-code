#!/usr/bin/python

f = open("input", "r")
input_str = f.read()

floor = 0 

for c in input_str:
	if c == '(':
		floor += 1
	if c == ')':
		floor -= 1

print floor
