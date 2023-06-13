#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes as c
import sys

_get_dict = c.pythonapi._PyObject_GetDictPtr
_get_dict.restype = c.POINTER(c.py_object)
_get_dict.argtypes = [c.py_object]


def find_class(type_name):
	for m in sys.modules.values():
		s = m.__dict__.get(type_name, None)
		if s is not None:
			return s
		
	raise NameError(f'Class {type_name} not found for extension')
	

class Extension():
	def __init__(self, cls):
		self.cls = cls
		cls_name = cls.__name__
		self.old = find_class(cls_name)
		self.inject()
		
	def __call__(self, *args, **kwargs):
		return self.old.__call__(*args, **kwargs)
	
	def inject(self):				
		_dict = _get_dict(self.old).contents.value
		for k, v in self.cls.__dict__.items():
			if k not in ('__module__', '__dict__', '__weakref__', '__doc__'):
				_dict[k] = v
		