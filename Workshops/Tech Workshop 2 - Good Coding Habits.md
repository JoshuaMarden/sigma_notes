___
__Internal Style Guide__
- [https://coda.io/d/Trainees_dryBdidTdcn/Code-Style-Guide_suBej#_luf2v](https://coda.io/d/Trainees_dryBdidTdcn/Code-Style-Guide_suBej#_luf2v)

__PEP8 Style Guide__
[https://pep8.org/](https://pep8.org/)

- Code is read more than it is written

Here we mindpool on why it is important
https://app.excalidraw.com/l/6gPaBlSh8PG/6713AtOeoBd

Looked at this code of an example of bad code:
```
import random def check(word, guess): # Do not fill this in yet pass def gen_wor(wlist): return random.choice(wlist) def func(): i = gen_wor() go = 5 while go > 0: input1 = input("Enter your guess: ") if len(i) != 5: print("Please enter a 5-letter word.") continue result = check(i, input1) print(' '.join(result)) if input1 == i: print("Congratulations! You've guessed the word.") return go -= 1 print(f"Sorry, you didn't guess the word. The word was {i}.") list2 = ["apple", "place", "grape", "chair", "spear", "green", "plant", "house", "water", "money", "tiger", "panda"] func(list2)
```

Use PyLint to and autopep8


`autopep8 --in-place my_script.py
`pylint my_script.py`