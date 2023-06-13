# Extensions


Extensions is a [common feature](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/extensions/) in Swift language. It enables to extend a class or a type to add it methods or attributes. 

This lab aims to add this feature to Python, using a CPython trick, making possible to extends even built-in types such as strings, int or lists !

### Example


```python
from Extensions import Extension

# Add a "length" property to strings
@Extension
class str:
	@property
	def length(self):
		return len(self)
		
print ('Hello, World!'.length)
# Output: 13
```