# Get your code online

We use Pythonanywhere because it is very friendly to people who have not much experience in administration and hosting. There is still a learning curve though and you will be required to do a few things in the shell (through a web interface in the browser), but I'll guide you through it.

Python Anywhere also has really [good documentation](https://help.pythonanywhere.com/pages/). What follows is the step-by-step guide how to get this specific app online. You have to replace the parts that are specific to my username with your username, which means that everywhere where it says **obstwalter** you have to put in your username instead.

# Creaete an account on Pythonanywhere 

Keep in mind that the username will be a part of the url - e.g. if your username is "batman83" your app will be reachable at https://batman83.pythonanywher.com. If you switch to a paid plan you can connect any domain you own to your web app.

# Create the Web app

Log into [Pythonanywhere](https://pythonanywhere.com) with your account credentials
In the web app choose to create a web app choosing the Manual configuration method.

If you run into trouble there is some more help here: [I've got an existing web app that I'm trying to deploy](https://help.pythonanywhere.com/pages/#ive-got-an-existing-web-app-that-im-trying-to-deploy).
 
# Fetch code from Github

Open a **Bash** Console from your dashboard.

type:

    $ git clone https://github.com/obestwalter/codecats-cv.git
    $ mkvirtualenv codecats-cv --python=/usr/bin/python3.5
    $ cd codecats-cv
    $ pwd
    
Copy the output of pwd which is the absolute path to the code of your web app (in my case it is `/home/obestwalter/codecats-cv` in your case it will be similar but with your username in the path).
 
Click on the "Dashboard" link and got to the "Web" Tab.

Go to the **Code:** section, click on **Source Code** and copy the absolute path to your checkout into the field.

# Congfigure WSGI app

    import sys
    
    path = '/home/<your username here>/codecats-cv'
    if path not in sys.path:
       sys.path.insert(0, path)
    from codecats_cv.controller import app as application

