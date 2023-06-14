# Lambda expressions

This is an implementation of an easier way to write anonymous functions in Python.

### Example


```python
from Expressions import _
		
l = [2, 4, 6, 8]		
		
triples = map(3 * _ + 1, l)
print ([*triples])
# Output: [7, 13, 19, 25]
```