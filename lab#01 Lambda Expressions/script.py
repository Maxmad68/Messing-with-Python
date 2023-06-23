#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Expressions import _

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

funct = 2 * _ + 1 # similar to "lambda x: 2 * x + 1"
print ("2*2+1=", funct(2)) 
print ("2*3+1=", funct(3)) # = 2*3+1 = 7
print ([*map(funct, l)])

even = filter(_ % 2 == 0, l)
print ("Evens :", [*even])


triples = map(3 * _, l)
print ("Triples :", [*triples])

