___

See [Excalidraw Doc](https://app.excalidraw.com/l/6gPaBlSh8PG/Agp4IoDKOju) for notes thus far.

The encapsulation and hiding of mechanisms and controls from the user that they do not need. Used to keep a simple interface, hiding complexity.

Makes for better code, as it is easier to use and harder to break. Useful for other developers.


## Getter & Setter
___

- Programmes can get very large with thousands of classes. 

- So you lock away as many variables inside the classes to keep things simple.

- variables with an underscore `_my_var` are not meant to be edited manually.

- Instead you have a `settr` function which sets the variable (it may do many things including error checking so it's important you use it.)

- Then you have a `gettr` function. This returns the variable so you can see what is in it.

- You use decorators `@property` to set the gettr function, and `@<var_name>.settr` to set it.

Example:

```python
class Dog:

  

	def __init__(self, age: int, owner: str, weight: int):

	self._age = age

	self._owner = None

	self.weight = weight

  

	@property   #   <-  gettr function returns `_age` 

	def age(self) -> int:

		return self._age

  

	@age.setter   #   <-  gettr function sets `_age` after some logic checks

	def age(self, new_age: int):

		if new_age - self._age < 1:
		
		    raise ValueError("Cannot set age")

		else:

			self._age = new_age

```
