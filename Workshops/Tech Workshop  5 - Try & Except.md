___

__Try__ & __Except__ can be used to flag errors that you are anticipating:

e.g. 

```python
try:
	my_index = my_list[142]
except IndexError:
	print("The list is too short, that index does not exist")
```

or 

```python
try:
	my_index = my_list[142]
except IndexError as the_error:
	print(the_error) 
```




This can be used to prevent the programme from simply crashing. For example:

```python


def get_user_input(prompt: str) -> int:
    number = input(prompt)

    if not number.isnumeric():
        raise ValueError ("Can only accept numerical characters")


while True:
    try:
    .   guess = get_user_input("Enter your guess: ")
            
        if result == "Correct!":
            break
        
    except ValueError as e:
        print(e)

```        

Here we can use an assertion to create a specific error message for what the user has done wrong. We then use a Try/Except nested in in a while loop so that the error can be printed but the programme doesn't crash - the user gets another shot to respond to the question.