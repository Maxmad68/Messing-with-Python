#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Jumps import goto, label


print (1)
goto .coucou

print (2) # Won't be executed

label .coucou
print (3)


a = 0
if a == 1:
	print ("This won't be printed")
	label .lol
	print ("This will be executed")
else:
	goto .lol
	print ("This won't be executed")