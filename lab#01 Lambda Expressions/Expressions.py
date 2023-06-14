#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Expression(object):
	def __init__(self, func):
		self._func = func
		self._arg_idx = -1
		
	def __call__(self, *par_args, **par_kwargs):
		if self._arg_idx == -1:
			l = par_args
		else:
			l = (par_args[self._arg_idx],)
		return self._func.__call__(*l,
								   **par_kwargs)
	
	def _(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__call__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __matmul__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__call__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __name__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__name__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __doc__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__doc__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __package__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__package__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __loader__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__loader__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __spec__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__spec__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __file__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__file__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __cached__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__cached__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __builtins__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__builtins__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __all__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__all__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __lt__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__lt__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __le__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__le__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __eq__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__eq__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __ne__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__ne__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __ge__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__ge__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __gt__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__gt__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __not__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return not self(*args, **kwargs).__not__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __abs__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__abs__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __add__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__add__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args]
				, **par_kwargs)
		
		return res
	
	def __radd__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__radd__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __and__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__and__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rand__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rand__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __floordiv__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__floordiv__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rfloordiv__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rfloordiv__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __index__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__index__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __inv__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__inv__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __invert__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__invert__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __lshift__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__lshift__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __mod__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__mod__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rmod__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rmod__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __mul__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__mul__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rmul__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rmul__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __neg__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__neg__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __or__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__or__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __ror__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__ror__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __pos__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__pos__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __pow__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__pow__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rpow__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rpow__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rshift__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rshift__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __sub__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__sub__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rsub__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rsub__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __truediv__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__truediv__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __rtruediv__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__rtruediv__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __xor__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__xor__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __concat__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__concat__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __contains__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__contains__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __delitem__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__delitem__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __getitem__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__getitem__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __setitem__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__setitem__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	def __int__(self, *par_args, **par_kwargs):
		@Expression
		def res(*args, **kwargs):
			return self(*args, **kwargs).__int__(
				*[a(*args, **kwargs) if isinstance(a, Expression) else a for a in par_args], **par_kwargs)
		
		return res
	
	# def __bool__(self):
	# 	@Expression
	# 	def res(*args, **kwargs):
	# 		return self(*args, **kwargs).__bool__()
	# 	return res
	
	def __repr__(self):
		return "<expression {}>".format(self.__prepr__())
	
	def __getattribute__(self, o):
		if o in ('_func', '_', '_arg_idx', '__repr__', '__prepr__'):
			return object.__getattribute__(self, o)
		
		@Expression
		def res(*args, **kwargs):
			obj = object.__getattribute__(self(*args, **kwargs), o)
			return obj
		
		return res
	
	
def create_argument_unity(arg_idx):
	@Expression
	def unity(x):
		return x
	
	unity._arg_idx = arg_idx
	return unity

def create_multiple_argument_unities(a, b = None):
	if b is None:
		return [create_argument_unity(i) for i in range(a)]
	else:
		return [create_argument_unity(i) for i in range(a, b)]
	
def ensure_unities(a, b = None):
	if a < 1:
		raise ValueError("a must be greater than 0")
		
	if b is None:
		a, b = 1, a
		
	l = []
	for i in range(a, b + 1):
		n = ("_%d" % i) if i > 1 else "_"
		unity = create_argument_unity(i - 1)
		l.append(unity)
		sys.modules['__main__'].__dict__[n] = unity
	return l


_, _2, _3 = ensure_unities(3)
