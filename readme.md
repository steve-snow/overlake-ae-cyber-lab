# Encrypting Password Logins

You will modify the security.js or security.py file only

Please replace them from the originals folder when you are done with exercise

## Video tutorial links

```
Getting latest version through Git repo  https://youtu.be/tQeC1VLKBss
Github repo  https://github.com/steve-snow/overlake-ae-cyber-lab

Python password hasing using Bcrypt  https://youtu.be/XwoxpkQvPNs
Javascript password hasing using Bcrypt  https://youtu.be/mjbpZmnVkzQ

```

## Javascript

- Install Node.js (current code testd on v22.13.1)
- Install Visual Studio Code
- Install Git Bash for Windows
- Test run to make sure the code runs
  - Open the terminal
  - Navigate to the ./passwordprotecting/javascript folder
  - `npm install`
  - change directory to subfolder `/main`
  - `node pasword-test.js`
  - This file is the test runner to know if you have successfully completed the task and defaults to only showing level 1 testing
- Modify the `security.js` file methods following the suggestions to complete the task

## Python

- Install Python 3
- Install Visual Studio Code
- Install Git Bash for Windows
- Test run to make sure the code runs
  - Open the terminal
  - Navigate to the ./passwordprotecting/javascript folder
  - `python pasword-test.py`
  - This file is the test runner to know if you have successfully completed the task and defaults to only showing level 1 testing
- Modify the `security.py` file methods following the suggestions to complete the task

## Raising the Level

- Add the number `2` to move on to the next phase of work.
- `node pasword-test.js 2` or  `python pasword-test.py 2`

## Installation Links

- Node.js  - V24 (LTS), Windows, Chocolaty, npm ``` https://nodejs.org/en/download ```
  - if the Chocolaty install through Powershell fails, it doesn't seem to effec the operation of the NPM commands, so just move along

- Python 3    ``` https://www.python.org/downloads/ ``` Download Python install manager
  
- Visual Studio Code  ``` https://code.visualstudio.com/download ``` select big blue Windows 10, 11 button
  - add desktop icons and context menu items

- Git Bash for Windows ``` https://gitforwindows.org/ ``` Blue Download button
  - Do add context menu options and similar, try not to limit yourself arbitrarily
  - Select VS Code or, if installed Notepadd ++ for commit editor - don't use VIM unless you are already comfortable with it
  - After the editor is selected, you can roll with the defaults for the rest of the the options

## Setting up Repo in lieu of copying folder from thumb drive

1. Navigate using Windows Explorer to the folder you want the git repo to live in 

2. Right click in the folder not on a file, select Show mor eoptions

3. Select Open Git Bash here

4. Git Bash for Windows terminal opens with the folder path showing above the prompt

5. To clone the repo the first time - Type or paste the following string into the terminal and press the Enter key

```
git clone https://github.com/steve-snow/overlake-ae-cyber-lab.git
```

6. Navigate into the new folder created:

```
cd overlake-ae-cyber-lab
```

7. You should now see "(main)" branch name trailing the folder in the prompt in the terminal

## Getting latest repo code

1. Open Git Bash terminal in Windows or from a Visual Studio Code instance open to a folder within the repo you wish to update


2. Check for changes (red or green file names)

```
git status
```

3. If you have chagned files indicated, try to use the Git sidebar menu (icon has three small circles with lines between them) to discard them so you can pull in the latst changes.

3. If you haven't changed any files in the repo, you can:

```
git pull origin main
```

The update may fail if you have changed files.  Discarding the changes should allow you to advance.

DO NOT COMMIT any of your changes (git add / git commit), just discard them using the git menu in the side bar

