___

This is a very, very crude breakdown of important concepts from the final workshop.

Remember: `instance methods` are functions that affects a _single_ instance of class, an object. Very, very limited scope.
### Class Methods
___

A method that will be applied across all instances of the class and all child classes. So you can make broad changes.

Class methods can change variables in already created child-classes. So you can tweak variables like Fuel:Oxygen ratio's across all types of thrusters without having to manually change every single rocket you have created.

```python
class Classroom:
	students_count = 0 # This keeps track of how many students are in the class

	@classmethod
	def add_student(cls):
		cls.students_count += 1 # This method will update the students_count

  
# Let's add some students and see the count
Classroom.add_student()
Classroom.add_student()

print(Classroom.students_count) # Output: 2
```

As that example is pretty pants (you could do that with an `instance method` easily enough) here is a better example:

```python
class Classroom:
	students_count = 0

	@classmethod
	def add_student(cls):
		cls.students_count += 1


class MathClass(Classroom):
	students_count = 0

class ScienceClass(Classroom):
	students_count = 0

# Each subclass can now manage its own students_count
MathClass.add_student()
MathClass.add_student()
ScienceClass.add_student()

print(MathClass.students_count) # Output: 2
print(ScienceClass.students_count) # Output: 1
print(Classroom.students_count) # Output: 0, the base class is unaffected
```
The MathClass Class has two people added. No instance of MathsClass exists yet but it will be initiated with at least two students. Not so for Science Class.

### Static Method
___

Static methods belong to a class, not an instance of the class. __They do not access the instance of the class itself__. It's just a function (class-method) that is only relevant to the class it is a part of, and doesn't need any objects to have been initiated to run.

For example, you could write a static method that would print information about the class.
Then you could find out about it before initiating it.

You might use a static method for formatting inputs, or to provide constants. These would be required and be the same across all instances of child classes.

```python
class Car:
	@staticmethod
	def is_valid_vin(vin):
		# VIN is a 17 Char string.
		return isinstance(vin, str) and len(vin) == 17
  
# You can call this method without creating a Car object
print(Car.is_valid_vin('1HGCM82633A004352')) # Output: True
print(Car.is_valid_vin('123')) # Output: False
```
Above, the check is applied to the attribute. It doesn't change anything, it just runs a check. It can be applied without instantiation of a single car object.


### Abstract Classes
___

Cannot be called itself, but lays out rules / a template for child classes that act as blueprints that can be called to create objects.

An abstract recipe class `meat_2_veg` might demand that a recipe requires a 'complete protein' (meat), but only the specific subclasses beneath that actually specify what meat to use / how much etc. `meat_2_veg` is never a real recipe, it's never an instantiated object, but the real recipe's inherit rules from it.

Here's an example with a toy that has the function`play`.

```python
from abc import ABC, abstractmethod

class Toy(ABC):
	def __init__(self, name):
		self.name = name

@abstractmethod
	def play(self):
		pass

# Subclass Car that inherits from Toy
class Car(Toy):
	def __init__(self, name):
		super().__init__(name)

	def play(self):
		return f"Driving the {self.name}"

# Subclass Doll that inherits from Toy
class Doll(Toy):
	def __init__(self, name):
		super().__init__(name)

	def play(self):
		return f"Dressing up the {self.name}"

# Creating instances
race_car = Car("Race Car")
barbie_doll = Doll("Barbie")
  
# Using the play method
print(race_car.play()) # Output: Driving the Race Car
print(barbie_doll.play()) # Output: Dressing up the Barbie
```

'ABC' stands for Abstract Base Class.

Basically, the abstract toy class has FORCED subsequent toy classes to have a play function. A developer who wanted to make a toy without a 'play' function would cause a crash. This is a good thing. No developer should be making toys that cannot be played with - it wouldn't be a toy at all.