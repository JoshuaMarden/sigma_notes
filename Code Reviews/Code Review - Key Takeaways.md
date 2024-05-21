___


__Linfan__

- Some cases of DRY
- Reminded me not to do
	`if x == y and z == y:`
	Can do :
	`if x == z == y:`
- Some cases in which function really ought to be decomposed
- Good use guard clauses
- Try to avoid indenting where possible
- Rather than having `21` set a var as `max_score` or something.
	 Don't have special numbers/strings.
	 You __CAN__ use a _global variables_ to give sensible names to important and unchanging
	 variables. Like number of hours in a day or card suits etc.
- You can joins lists like this `[list_a, ...list_b, ...list_c]` so that the resulting list is not a list of nested lists, but a list containing the elements of a, b, and c.


__Krzysztof__

- Keep functions small (though some good decomposition)
- great use dicts
- if you have two different values as options, have a `True`/`False` option with a named variable to make code more readable.


__Key TakeAways__

Don't use magic numbers. Use Global variables.
