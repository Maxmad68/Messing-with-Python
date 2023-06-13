#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Extensions import Extension


# Add a "length" property to strings
@Extension
class str:
	@property
	def length(self):
		return len(self)


# Add a "say_hi" method to int instances
@Extension
class int:
	def say_hi(self):
		parity = (' even', 'n odd')[self%2]
		print (f'Hello, I\'m {self} ! I\'m a{parity} number')
	
	


print ('Hello, World!'.length)

an_integer = 42
an_integer.say_hi()