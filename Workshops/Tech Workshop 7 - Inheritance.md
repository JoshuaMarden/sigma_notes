___

- Often the best way to go about using classes is to create a parent class. Subsequent, related classes can inherit it's atrtreibutes.

In the example below I have declared an animal class, and then made child-derivatives of it.

```python
# Parent

class Animal:
	def __init__(self, name: str, weight: int):
		self.name = name
		self.weight = weight

# Child
class Dog(Animal):
	def __init__(self, name: str, weight: int):
		super().__init__(name, weight)
		
	def bark(self):
		if self.weight > 100:
			print("WOOF")
		else:
			print("woof")

# Child
class Cat(Animal):
	def __init__(self, name: str, weight: int):
		super().__init__(name, weight)

def meow(self):
	if self.weight > 10:
		print("MEOW")
	else:
	    print("meow")
```

- A useful concept is __method overriding__. This is where you use the same function name across classes, but they do something slightly different depending on the class.

In the example below, all classes have a function by which they make (print) a sound. But it changes depending on the child.

```python
class Animal:
	def __init__(self, name: str, weight: int):
		self.name = name
		self.weight = weight

	def makes_sound(self):
		print("*bumps glass*")

# Child
class Dog(Animal):
	def __init__(self, name: str, weight: int):
		super().__init__(name, weight)
		
	def makes_sound(self):
		if self.weight > 100:
			print("WOOF")
		else:
			print("woof")

# Child
class Cat(Animal):
	def __init__(self, name: str, weight: int):
		super().__init__(name, weight)

	def makes_sound(self):
		if self.weight > 10:
			print("MEOW")
		else:
			print("meow")
```


- For method overriding Chris recommends always using the same arguments so that when you are trying to call a function you don't have to guess what the number of necessary arguments are. 


- Using flow diagrams to plan for parent-child class trees is a really good way of understanding what functions and what attributes are required at different heights in the parent-child tree.