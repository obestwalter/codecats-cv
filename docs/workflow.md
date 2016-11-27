# Development workflow

## Development

* fork this repo into your own Github account
* clone your repo on your devbox
* create a Python3.5 virtualenv and activate it
* install app in virtualenv (`pip install -e <path/to/repo/clone>`)
* set virtualenv as Project Interpreter in PyCharm
* run `controller.py` (starts a local devserver)
* make changes
* check in Browser if it works
* commit and push changes to Github

## Deployment

Go to pythonanywhere and open a Bash console.

In Bash console:
    
    $ cd ~/codecats-cv
    $ git pull
    
Go to Dashboard > Web and reload the app.
