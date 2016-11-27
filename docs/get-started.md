# Get started

## Get your code online

We will deploy the app on [pythonanywhere](https://pythonanywhere.com) because it is very friendly to people who have not much experience in administration and hosting. 

* Cost free plan is already powerful enough to host a simple web app that does not have too much traffic
* Already includes a URL (`https://<your pythonanywhere username>.pythonanywhere.com`) to have a site online in minutes

There is still a learning curve though and you will be required to do a few things in the shell (through a web interface in the browser), but I'll guide you through it.

Python Anywhere also has really [good documentation](https://help.pythonanywhere.com/pages/). What follows is the step-by-step guide how to get this specific app online. 

**NOTE:** In paths you have to replace the parts in angled brackets  (**\<your username\>**) with your pythonanywhere username.

## Create an account on pythonanywhere 

Keep in mind that the username will be a part of the url - e.g. if your username is "batman83" your app will be reachable at `https://batman83.pythonanywhere.com`. If you switch to a paid plan you can connect any domain you own to your web app.

# Create the Web app

* Log into [pythonanywhere](https://pythonanywhere.com) with your account credentials.
* In the web app tab create a web app choosing the Manual configuration method. 
* Choose Python3.5 as interpreter

Now you have an app that needs to be further configured.

# Create a virtualenv for the app

Go to the "Consoles" tab and Open a **Bash** Console from your dashboard.

In Bash console:

    $ cd ~
    $ mkvirtualenv codecats-cv --python=/usr/bin/python3.5
    $ cd .virtualenvs/codecats-cv
    $ pwd

Copy the output of pwd which is the absolute path to the virtualenv (`/home/<your username>/.virtualenvs/codecats-cv`) into your clipboard.
 
Click on the "Dashboard" link and got to the "Web" Tab. 

Go to the **Virtualenv:** section, click on **Source Code**, copy the path from your clipoard into the field and klick the checkmark next to the field to save the change.

If the path is correct a link will turn up directly below the virtualenv path: "Start a console in this virtualenv" - click on the link to got to a bash console with the active virtualenv.

# Fetch code from Github

In Bash console:

    $ cd ~  # change into your home directory
    $ git clone https://github.com/<your username>/codecats-cv.git
    $ cd codecats-cv
    $ pip install -e .  # installs the app
    $ pwd
    
Copy the output of pwd which is the absolute path to the code of your web app (`/home/<your username>/codecats-cv`) into your clipboard.
 
Click on the "Dashboard" link and got to the "Web" Tab.

Go to the **Code:** section, click on **Source Code**, copy the path from your clipoard into the field and klick the checkmark next to the field to save the change.

# Congfigure WSGI app

Go to the **Code:** section, click on the path in **WSGI configuration** you can edit that file directly in the web browser then. Delete all the contents and replace them with this:

```Python
import sys

path = '/home/<your username>/codecats-cv'
if path not in sys.path:
   sys.path.insert(0, path)
from codecats_cv.controller import app as application
```
**Do not forget to replace **<your username>** with your actual username.

# Set path for static files

Not necessary but makes your app load faster.

Go to Dashboard > Web and add

# Set a password

If you want your CV to be only accessible to specific people you can also set a password in Dashboard > Web (Web app needs to be reloaded to activate protection).

This makes only sense though if you also keep the private data out of your Repository.

# Troubleshooting

If you run into trouble there is some more help here: [I've got an existing web app that I'm trying to deploy](https://help.pythonanywhere.com/pages/#ive-got-an-existing-web-app-that-im-trying-to-deploy).
 
