___

1. Go to home
	`/Users/<account_name>`

2. Open the shell configuration
    `nano ~/.zshrc`

3. Add an alias and path to your helper file e.g.
	`alias jogmymemory='/Users/<account_name>/Documents/Sigma/jogmymemory.sh'` 
	
	A really good place to put this helper file at some point would be here:
	`/usr/local/bin/jogmymemory.sh`

4. You save and exit nano using:  [ctrl] + [x]  >  [y]  >  [enter].

5. Get the terminal to update and recognise this new command:

	 `nano ~/.zshrc`

7. You may need to make sure it's an executable:
	`chmod +x /Users/<account_name>/Documents/Sigma/jogmymemory.sh`

___

###  Example `jogmymemory.sh`

```bash
#!/bin/bash

echo " "

echo " "

echo " -------------------------------- * --------------------------------"

echo " ---> GitHub Repo for Notes:"

echo "https://github.com/JoshuaMarden/sigma_notes"

echo " ---> Unobtrusive music when coding:"

echo "https://www.youtube.com/watch?v=m80E1K75vDI"

echo " -------------------------------- * --------------------------------"

echo "---> How to upload projects to a new git repo:"

echo "\`git init\`"

echo "\`git add .\`"

echo "\`git commit -m "initial commit"\`"

echo "\`git remote add origin <REMOTE_REPOSITORY_URL>\`"

echo "\'git git push -u origin master \`"

echo " -------------------------------- * --------------------------------"

echo "---> How to clone a repo:"

echo "\`git clone <remote REMOTE_REPOSITORY_URL>\`"

echo "---> Then change direcotyr into new folder using \`cd\`"

echo "\`git fetch origin\`"

echo "\`git pull origin <branch_name>\` (should be \`main\` for default)"

echo "\`git fetch origin\`"

echo "\'git pull origin main\`"

echo " -------------------------------- * --------------------------------"

echo "How to create and activate a virtual environment:"

echo "\`1. python3 -m venv <myenv>\`"

echo "\`2. source <myenv>/bin/activate\`"

echo " -------------------------------- * -------------------------------- "

echo "---> How to run an individual test unit with pytest"

echo "\`pytest <file_name>.py::<test_name>\`"

echo "---> How to run tests that match a keyword"

echo "\`pytest -k <keyword>\`"

echo "---> How to view the full output of a test:"

echo "\`pytest -vv <file_name>.py\`"

echo " -------------------------------- * -------------------------------- "

echo "---> List hidden files:"

echo "\`ls -lhf\`"
```