#python #coding 


Store of useful lines and snippets, things I might want to remember, or things I almost remember but misuse regularly.

Note that to prevent obsidian linking internally double square brackets have to be escaped using a backslash, making some of the lines technically incorrect.


---

## `.join()` and `.split()`


You could combine these split a string up if the would-be elements haven't been separated in the same way.

```
string = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friendsList = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friendsList)
```

`['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']

note that `.replace()` would work too:

`print(csv.replace(';',',').replace(':',',').split(','))

---

### Simple Membership Test

Check if elements are in a set without a loop.

```
mySet = {'John','Michael','Terry','Eric','Graham','Eric'}
print('Eric' in mySet and 'John' in mySet)
```

`True`

---

## Join `sets

to join use:

`print(setA.union(setB))

or

`print(setA | setB)`

---

## `.intersection()` , `.difference()`, & `symmetric_difference()`

Will find either which elements are in two _SETS_, or which elements are present in one one _SET_
```
setA = {'John','Michael','Terry','Eric','Graham','Eric'}
setB = {'Reg','Loretta','Colin','Eric','Graham'}  

print(setA.difference(setB))
```


`{'John', 'Michael', 'Terry'}


You can check for elements that are only in one set (setA in example) using by using the following instead of `.difference()`:

`print(setA - setB)

`{'Michael', 'Terry', 'Eric'}


You can check for matching elements using by using the following instead of `.intersection()`:

`print(setA & setB)

`{'John', 'Graham'}`


You can check for elements that are unique to each list:

`print(setA.symmetric_difference(setB))
OR
`print(setA ^ setB)

`{'Reg', 'Loretta', 'Colin', 'Michael', 'Terry', 'Eric'}

---

## `.sort()` vs `.sorted()`


`.sort()` will sort a list

`.sorted` will return a new, sorted object. It can be used on immutable objects as it returns a new list object entirely.

It can be useful for immutable objects like dicts:

example:
`my_dict = {'car':4,'dog':2,'add':3,'bee':1}`


`print(sorted(my_dict)`
returns:  
`['add', 'bee', 'car', 'dog']`


`print(sorted(my_dict.values()))`
Returns:
`[1, 2, 3, 4]`


`print(sorted(my_dict.items()))`
Returns:
`[('add', 3), ('bee', 1), ('car', 4), ('dog', 2)]`


The sort method desired can be put after sorted under `key`:
`my_list_of_lists=\[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

`print(sorted(my_list_of_lists, key = lambda item :item[0]))`
Returns:
`\[['add', 3, 10], ['bee', 1, 24], ['car', 4, 65], ['dog', 2, 30]]
Because it sorts using the first item.


`print(sorted(my_list_of_lists, key = lambda item :item[2]))`
Returns:
`\[['add', 3, 10], ['bee', 1, 24], ['dog', 2, 30], ['car', 4, 65]]
Because it has sorted by the third item.

---

## Notes on Dictionaries


```
movie = {
  'title' : 'Life of Brian',
  'year' : 1979,
  'cast' : ['John','Eric','Michael','George','Terry']
}
```

You can use `.get()` to get items from a dict, and if nothing is not returned, a default message can be returned instead (`None` if left blank). This is better than an error.

`print(movie.get('budget','not found'))
Returns:
`not found`

To update existing:
`movie['title'] = 'The Holy Grail'
or
`movie.update({'title' : 'The Holy Grail','year':1975

To add data:
`movie['budget'] = $4 million

To delete:
`del movie['year']
Pop works too:
`year = movie.pop('year')`

Obviously you can also use `.keys()`, `.values()` &  `.items()`

Loop:
`for key, value in movie.items():
`print(key, value)`

---

## Joining Dictionaries

Dictionaries can be joined:
```
python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}
```

`people = {}
`people.update(python)
`print(people)
Returns:`{'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}


Or we can use a comprehension:
`for groups in (python,holy_grail) : people.update(groups)
Returns:
`{'TerryG': 34, 'Graham': 37, 'Terry': 38, 'Michael': 35, 'Eric': 36, 'John': 35, 'Zoot': 17, 'Knight of NI': 40, 'Lancelot': 39, 'Galahad': 35, 'Arthur': 40}


Or we can use unpacking with `**`
`people = {**python,**holy_grail,**life_of_brian}
`print(people)`
Returns:
`{'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34, 'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17, 'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'Biccus Diccus': 45}


---

## Reading Text Files

Basic way of opening the file:
`my_file = open('greeting.txt','r')
(r is for read, w would be write, a would be append)


Print up-to a character index:
`print(my_file.read(10))


Print first line:
`print(my_file.readline())


print second line:
`print(my_file.readline())
(weirdly it keeps track)


Lines to a list:
`linesAsList = my_file.read().splitlines()
`print(linesAsList)
(note that `readlines` can also do this.)


IMPORTANT: close the file after:
`my_file.close()


BETTER: Don't open and close it manually, only have it open while you use it:
`with open('friends.csv','r') as f:
`    # Do x`

---

## Try / Except

```
try:

    #code you want to run

except:

    #executed if error occurs

else:

    #executed if no error

finally:

    #always executed

```


Example with code:
```

try:
    num=int(input('Enter a number between 1 and 30: '))
    num1 = 30/num

if num > 30:
    raise ValueError(num)

except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")

except ValueError as err:
    print(err,num, "Bad Value not between 1 and 30!")

except:
    print("Invalid Input!")

else:
    print("30 divided by",num, "is: ", 30/num)

finally:
    print("**Thank you for playing!**")
```
*note how the if statement can be used to call certain errors*
*note that multiple excepts are possible for different errors*

---

## Classes

Classes are a way to create your own complex data type.

Below is an example of a class with it's own variables and even a function.
```
class general:
    def __init__(self, name, nickName, dob, dod, pitchedBattles, victories):
        self.name = name
        self.nickName = nickName
        self.dob = dob
        self.dod = dod
        self.pitchedBattles = pitchedBattles
        self.victories = victories

    def print_overview(self):
        print("Name: ", self.name)
        print("Nick Name: ", self.nickNames)
        print("Date of Birth: ", self.dob)
        print("Deceased: ", self.dod)
        print("Recorded, pitched battles: ", self.pitchedBattles)
        print("Victories", self.victories)
    
```


Below is an example of how to create an object from the class:
```
dukeOfWellington = (Sir Arthur Wellesley, Iron Duke, 1769, 1854,  15, 15)

```


Class variables can be accessed like so:
`print(dukeOfWellington.name)`
Returns:
`Sir Arthur Wellesley`


Call the internal function like so:
`dukeOfWellinghton.print_overview()`
Returns:
```
Name: Sir Arthur Wellesley
Nick Name: Iron Duke
Date of Birth: 1769
Deceased: 1854
Recorded, pitched battles: 15
Victories: 15
```
*Note: if you now try* `general.print_overview` *it will print it again, as the last accessed object remains in the memory.*


In a class...
variables are called **attributes**
functions are called **methods**


---

## Inheritance with classes

Create a class:
```
class tradingVessel:
    def __init__(self, name, nation, type, length):
        self.name = name
        self.nation = nation
        self.type = type
        self.length = length

cutty = tradingVessel("Cutty Sark", "Great Britain", "Clipper", 212.5)
```

Create a child class (and add an attribute):
```
class militaryVessel(tradingVessel):
    def __init__(self, name, nation, type, length, cannons):
        super().__init__(name, nation, type, length)
        self.cannons = cannons

vic = militaryVessel("HMS Victory", "Great Britain", "First-rate ship of the line", 227, 92)
```

---

## Zip

Zip can join lists into tuples and dicts.

Can be used to join lists:
```
nums = '1234'
letters = ['a','b','c','d']

combo = list(zip(nums,letters))
print(combo)
```
Returns:
`[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


Can join multiple lists:
```
nums = '1234'
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

combo = list(zip(nums,letters,names))
print(combo)
```
Returns:
`[('1', 'a', 'John'), ('2', 'b', 'Eric'), ('3', 'c', 'Michael'), ('4', 'd', 'Graham')]`

To unzip:
`num,let,nam =zip(*combo)


Can be used to make dicts:
`myDict = dict(zip(nums,letters))
So can this:
`myDict = {key:value for key,value in zip(nums,letters)}

To revert back to lists:
`nums, letters = list(myDict.nums()), list(myDict.letters())

---

## Randomness

To randomise (pseudo-randomise) use a module called `random`

```
import random
```

To generate 5 random numbers:
```
for i in range(5):
    print(random.random())
```

To generate 5 random numbers in a range?:
```
for i in range(5):
    print(random.uniform(1,6)
```

Want integers?
```
for i in range(5):
    print(random.randmint(1,6)
```

Range AND steps?
```
for i in range(5):
    print(random.randrange(1,100,2))
```

What about getting a random element from a list?
```
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))
```


using `random.choices` will draw randomly allowing for repeats. Using `random.sample` will not allow for repeats.

e.g.
`print(random.sample(friends_list,5))
Returns:
`['John', 'Terry', 'Michael', 'Eric', 'Graham']`

You can also shuffle the list:
```
random.shuffle(friends_list)
print(friends_list)
```
Returns:
`['John', 'Terry', 'Graham', 'Eric', 'Michael']


You can also generate random strings if you import `string`
```
import string, random

# Will create a list of all chars and integers
letters_numbers = string.ascii_letters + string.digits
```

Example:
```
word = ''
for i in range(7):
   word = word + random.choice(letters_numbers)

print(word)
```
Returns:
`bB90NNz

Note, you can specify upper or lowercase:
`string.ascii_uppercase
`string.ascii_lowercase`

---

## Timeit & Performance 

Performance and execution time for small snippets can be measured.

```
import timeit

def my_function()
	pass

print timeit.timeit("my_function")
```
The above will return a time.

Note that you can run multiple tests and get the average:
`print timeit.timeit("my_function", number = 10)
Will tests the code 10 times.

---

## Lambdas / Lambda functions

There are simple, one-line, anonymous functions.

`optional_name = lambda paramaters(s): expression
e.g.
`double_multiply = lambda x,y : 2*x*y

They do not need a name, and do not need to return anything.


```
# Another example

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

monty_python.sort(key = lambda name:name.split(' ')[-1])
```
Returns:
`['Graham Arthur Chapman', 'John Marwood Cleese', 'Terrence Vance Gilliam', 'Eric Idle', 'Terry Graham Perry Jones', 'Michael Edward Palin']
(Has been sorted by first name.)

---

## More on Lambdas / Lambda functions

A function can return a lambda function as it's output.

e.g.
```
def my_function(n):
	return lambda a : a*n

doubler = my_function(2)

print(doubler(2))

```
Returns
`6`

From there you could create a tripler and quintupler, e.g.
`tripler = my_function(3)
`quintupler = my_function(5)

This dynamically creates spin-off functions with their own names as you go along.

Another example:
```
def price_calc(start, hourly_rate):
	return lambda hours: start + hourly_rate * hours

walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)
```
Here you have created two different functions using the same equation with different values.

To expand yet further, here are a few ways you can write Lamba functions. All of the below add up to 9.
```
print((lambda a,b,c: a+b+c)(2,3,4))

print((lambda a,b,c=2: a+b+c)(2,3,4))

print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))

print((lambda *args: a+b+c)(2,3,4))
```

---
### Comprehensions

An evolution of lambdas/maps/filters to simply create objects.

Could be seen as a very concise way to avoid using a `for-loop`.

The layout looks like so:
``[expression for item in iterable if condition]``

e.g.
```
numbers = [1,2,3,4,5,6,7,8,9]

# For-Loop Version
new_list = []
for num in numbers:
	if num % 2 == 0:
		new_list.append(num*num)

# Comprehension version
new_list = [num for num in numbers if num % 2 == 0]
```

Another example with a dict:
```
movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail", "Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]


# Loop version
new_dict = dict()
for movie, yr in zip(movies,year):
	new_dict[movie] = yr

# Comprehension Version
new_dict = {movie:yr for movie,yr in zip(movies,year)}
```