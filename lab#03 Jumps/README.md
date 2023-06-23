# Jumps

Goto is an instruction present in several languages. It is a control flow statement that allows a program to jump to a labeled line of code, bypassing the normal sequential execution. It is considered a controversial feature due to its potential to make code less readable and harder to maintain.

Gotos are not present in Python, despite some implementations have been released on Github. This is another one of them.



### How to use ?

You can label a part of the code with `label .name`, and then go to the label with `goto .label`



### Example

```python
from Jumps import goto, label

print (1)
goto .coucou

print (2) # Won't be executed

label .coucou
print (3)
```