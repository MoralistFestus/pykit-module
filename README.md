# Pykit
Pykit is a module written with python that allows you to perform basic arithmetical operations without writing boilerplate codes. Pykit gives flexibility to your code by allowing you to perform magic functions with lists, dictionary, tuple, etc.

Pykit module can also perform some random generation such as generating random strings, numbers and keywords.

# Hello World
Simple Hello World program in pykit module:
	
```python 
import pykit
pykit.write("Hello World")
```

## Basic usage
Using pykit module is as easy as working with normal modules in python. You just have to use the Python `import` statement to import the module.

For example:
```python
import pykit
```

You can rename the module:
```python 
import pykit as pk
pk.write("Hello World")
```

Or use preferred name. 
You can import a specific attribute from the module

```python
from pykit import write
write("Hello World")
```
Another example:
```python
from pykit import multiply
a = int(input("Number1"))
b = int(input("Number2"))
print("Result is", multiply(a, b))
```
When you import a specific attribute you don't need to call the module name.

# Working with Pykit module 
You can perform basic arithmetical operation with pykit

For example:
```python
import pykit as pk
a = int(input("Enter first number"))
b = int(input("Enter Second number"))
print("Result = ", pk.subtract(a, b))
```

## Pykit Arithmetical Functions
Pykit module has different Arithmetical Functions, these includes:

- subtract(): Subtraction is pykit function that allows you to carry out minus operation. E.g a - b

- summation(): Summation is pykit function that carry out additional operation. E.g a + b

- divide(): For division operation. E.g a / b

- multiply(): For multiply operation. 
E.g a * b

For full documentation, Download the pdf book: [pykit-doc](https://)