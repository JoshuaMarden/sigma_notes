___
Up until now we have been writing code _procedurally_.

"Object Oriented Programming" - basically a logical method for coding that is easier and less abstract than original languages. OOP can help model the real world in our code and in our minds.

A key feature is that they use __objects__, such as __classes__, which act as blueprints. Classes have a name and then contain data that relates to them, as well as functions that are specific to them.
Instead of having the word "Chair" as a variable and then lots of materials and dimensions floating around as variables, you store "Chair" as a class. The class contains the material, height, width, No. legs, and functions such as "sit", "fold", or "swivel".

Code becomes more readable. More testable. More re-usable.

OOP is tool. It takes more time. Higher upfront cost. Greater payoff. Like TDD.

### Abstraction
___

- An idea or problem decomposed into relevant, related blocks.
	- A recipe is an __abstraction__ of a pie... The idea and its components are there, but a recipe is not a pie - it is a blueprint. The __instance__ would be the __pie__. 







From Procedural:

```python
def print_question(question: dict):

print(question['text'])

for i in range(0, len(question['values'])):

print(f"{i + 1}. {question['values'][i]}")

  
  

def ask() -> int:

user_answer_str = None

while user_answer_str == None:

user_answer_str = input(

'What is your answer? Please enter the number. \n')

try:

user_answer = int(user_answer_str)

return user_answer

except:

print("Please enter a number.")

ask()

  
  

def finish(final_score: int, total_score: int):

print(f'Your score is: {final_score} out of {total_score}')

  
  

question1 = {

'text': 'Who is the odd one out of Sigma Staff?',

'values': ['Harry', 'Sonali', 'Chris'],

'answer': 1

}

  

question2 = {

'text': "What is Chris' surname?",

'values': ['John', 'Owen', 'Gaston'],

'answer': 2

}

  

question3 = {

'text': 'What is the capital of China?',

'values': ['Beijing', 'Shanghai', 'Taipei'],

'answer': 1

}

  

question4 = {

'text': 'What is the tallest mountain?',

'values': ['k2', 'Mauna Kea', 'Everest'],

'answer': 3

}

  

round1 = {'name': 'Sigma Labs', 'questions': [question1, question2]}

  

round2 = {'name': 'Geography', 'questions': [question3, question4]}

  

rounds = [round1, round2]

  
  

def play():

score = 0

  

no_questions = 0

for round in rounds:

for question in round["questions"]:

no_questions += 1

print_question(question)

answer = ask()

is_correct = answer == question['answer']

if is_correct == True:

score += 1

print("Correct")

else:

print("Incorrect")

  

finish(score, no_questions)

  
  

play()
```


To Object Oriented using Classes:
```Python
class Player:

  

def __init__(self, name: str):

self.name = name

self.score = 0

  

def increase_score(self):

self.score = self.score + 1

  
  

class Question:

def __init__(self, question: str, answers: list[str], answer: int):

self.question_text = question

self.answers = answers

self.answer = answer

  

def is_correct(self, given_answer: int) -> bool:

return given_answer == self.answer

  
  

class Round:

def __init__(self, name: str, questions: list[Question]):

self.name = name

self.questions = questions

  
  

class Game:

  

def __init__(self, rounds: list[Round]):

self.rounds = rounds

  

def print_question(self, question: dict):

print(question.question_text)

for i in range(0, len(question.answers)):

print(f"{i + 1}. {question.answers[i]}")

  

def ask(self) -> int:

user_answer_str = None

while user_answer_str == None:

user_answer_str = input(

'What is your answer? Please enter the number. \n')

try:

user_answer = int(user_answer_str)

return user_answer

except:

print("Please enter a number.")

ask()

  

def finish(self, player: Player, total_score: int):

print(f'Your score is: {player.score} out of {total_score}')

  

def play(self):

name = input("What is your name? ")

player = Player(name)

  

no_questions = 0

for round in rounds:

for question in round.questions:

no_questions += 1

self.print_question(question)

  

answer = self.ask()

if question.is_correct(answer) == True:

player.increase_score()

print("Correct")

else:

print("Incorrect")

  

self.finish(player, no_questions)

  
  

if __name__ == "__main__":

question1 = Question('Who is the odd one out of Sigma Staff?', [

'Harry', 'Gloriose', 'Chris'], 1)

question2 = Question("What is Chris' surname?", [

'John', 'Owen', 'Gaston'], 2)

question3 = Question('What is the capital of China?', [

'Beijing', 'Shanghai', 'Taipei'], 1)

question4 = Question('What is the tallest mountain?', [

'k2', 'Mauna Kea', 'Everest'], 3)

  

round1 = Round("Sigma Labs", [question1, question2])

round2 = Round("Geography", [question3, question4])

  

rounds = [round1, round2]

  

game = Game(rounds)

game.play()
```