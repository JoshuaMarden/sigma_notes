## On Repo's & TDD
https://curriculum.sigmalabs.co.uk/Software-Fundamentals/Fundamentals/Week%201/Overview

Repo's are just code stores
TDD stands for Test Driven Developement
### Getting a Sigma Repo
___

1. Find repo
2. __Fork__ it to create a version on your github account
3. __Clone__ it to get it onto your own hardware / computer


This is how you get your code. 

__Note__: For our repo we have to enable `actions` manually as we are giving root access to Sigma. Bare this in mind in the future as it is important to do, but opens your code to other people.

### Push own work to fresh Repo
___
I'm pushing my notes to a repo as so:

Make Repo using GitHub GUI:
(Move to folder you wish to push)
`git init
`git add .
`git commit -m "first commit of notes"`
`git branch -M main
`git remote add origin https://github.com/JoshuaMarden/sigma_notes.git
`git push -u origin main
### Pushing to GitHub I
___
Check what is different on git vs on your machine:
`git status

Add all the files - git will know which ones have actually been changed (see also `ignore`)
`git add . 

Then you commit them with a sensible message
`git commit -m "sensible description of changes"

Finally, push them from the staging area to the online repo
`git push`

#### Pushing things to GitHub II
___
When you are pushing to GitHub, and you have activated `actions`, you are going to be running scripts and editing files on GitHub so they no longer match the files you have stored locally.

This can be seen if you run:
`git fetch

Your local files can then be updated with:
`git pull`

Enabling actions allow basic ratings of your code quality to be carried out automatically.

You can see this in the repo under `code_review/report.txt` if you want to have a look.

### Git Ignore and keeping private files private
___
A `.gitignore` file is a text file that tells Git which files or directories to ignore in a project. It's very useful for not including files that you don't want to commit to a repository, like personal environment settings or compiled files.

Here's a basic example of what the contents of a `.gitignore` file might look like:

```
# Ignore all log files *.log # Ignore node_modules directory used by JavaScript projects node_modules/ # Ignore all PDF files in a doc/ directory doc/**/*.pdf # Ignore all .venv files .env
```

#### Using a `venv` - Virtual Environment
___

__Note:__ `Homebrew` requires an environment! It does not want you downloading things outside of your environment. This makes sense but gives us another hurdle to jump through.

1. `python3 -m venv .venv
   _this creates a hidden (with `.` virtual environment)_
2. `source .venv/bin/activate
   _activates the environment with you running code inside_

If you do this you will need to use `pip3 install pytest` for example - because the environment will be clean and empty with no modules.

This basically acts as a shield so if you mess with the variables of the environment you aren't creating bugs for other scripts and programmes. Creates a sandbox/playground with fewer consequences.

### `PyTest` & TDD
___
For a proper overview of 'Targeted Development Goals' see course website.

Core:
1. Write a test
2. Run the test and watch it fail
3. Write the code to make it pass
4. [Refactor](https://www.agilealliance.org/glossary/refactoring/) the code to make it really good


This is the __RED__, __GREEN__, __REFACTOR__ process!!

Make a tests that fails, pass the test, improve the underlying code!!! 

`Pytest` is used for TDD.

```
# 1. Import the code you want to test  
from calculator import add_numbers  
  
# 2. Give the test a useful, plain english name  
def test_adding_2_and_10_should_equal_12():  
# 3. Write special "assert" functions that test to ensue that the code works as you expect it to  
assert add_numbers(2, 10) == 12
```

`pytest run example_script.py`
