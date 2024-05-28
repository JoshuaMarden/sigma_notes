___

__Mabon's Code__

- Well written, simple, clear.
- 1 bug suggests slightly better TDD is required.
- Raise errors not exceptions. Errors _are_ exceptions, use ValueErrors or something specific.
- Be careful with naming it can mislead other programmers.
- Do not have the same bit of code in an `If` and an `Else`, you are doing something wrong. DRY.


__Comments by Chris__

- Super() can be used when you have already used polymorophism to overwrite a parent function in your child. BUT, if you then want the original function, you can call it back with super(). So it is quite useful even when embedded deeper into the child class.

- You can print objects dierctly:
```
def __str__(self)
	return f"VHS: {self.video_name}"
```

This could make debugging _a lot_ easier because rather than being sent to a memory address you can Identify the object when you try `print(my_video_object)`.


- Repeating Getter's & Setter's
	-  These are used to hide variables from other developers. It makes them go through a specific hoops to get or set a variable.
	- `@property` just allows you to call a function that manipulated your `_private_var` without calling a function verbosely. You are in fact still calling a method, it's just hidden.
	- `@health.setter` Allows you to set a function without appearing to have called a function keeping that code clean.
	- You can actually just create a `set_var` and `get_var` function as your setter and your getter. And then you would call them as normal methods. 
