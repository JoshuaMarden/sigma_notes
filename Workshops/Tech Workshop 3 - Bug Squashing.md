___

### Errors:
____

1. Compiler errors
2. Syntax Errors
3. logic errors (Can run but unexpected outcome)

### Example Bad Code
___

```python
def ask_user_for_phone_number() -> str:  
user_input = input("What is the phone number to validate?")  
return user_input  
  
  
def main():  
phone_no = ask_user_for_phone_number()  
block_no = phone_no.contains(" ", "")  
formatted_number = convert_phone_to_UK_Format(phone_no)  
if len(formatted_number) > 0:  
print(formatted_number)  
else:  
print_invalid_input_error()  
  
  
def is_number_valid_length(phoneNo: str) -> bool:  
return phoneNo.length is 11  
  
  
def is_UK_number(phone_no: str) -> bool:  
return phone_no.slice(0, 1) is "07"  
  
  
def has_country_code(phone_no: str) -> bool:  
return phone_no.contains("+44")  
  
  
def convert_phone_to_UK_Format(input: str) -> list:  
phone_list = []  
if has_country_code(input):  
input.replace("+44", "07")  
  
if is_number_valid_length(input) and is_UK_number(input):  
phone_list = convert_string_to_phone_format(input)  
  
return phone_list  
  
  
def convert_string_to_phone_format(phone_str: str) -> list:  
phoneA = phone_str[0:5]  
phoneB = phone_str[6]  
return [phoneA, phoneB]  
  
  
def print_invalid_input_error():  
print("This is an invalid UK number. Please try again.")  
  
  
main()
```


Spotting bugs in above code:

`.contains` not valid method call

calling `convert_phone_to_UK_Format` function before defined

`main`should be at bottom really

`is_UK_number` is taking only the first digit not first two. Also ignores +44 ppossibility.

'`def is_number_valid_length(phoneNo: str) -> bool:  
return phoneNo.length is 11`

main should be in an if statement:
`if __name__ == "__main__":`

Name clash! Do not use `input` as a var name when it is a function.



### Errors:

1. Compiler errors
2. Sybntax Errors
3. logic errors

`is` works if the objects are immuatble and share the same memory space.