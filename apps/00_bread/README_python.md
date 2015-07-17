# The Python Environment

Python is known as the programming language that's the second best at everything. It is a programming designed around the idea that code is not for computers — code is for humans.

Most modern operating systems (OS) come with Python pre-installed, but because the versions and libraries can vary wildly, we utilize *virtual environments* to separate out our python installations. You can think of these as mini python installations.

There's good news and bad news about these virtual environments. The bad news is that they can be tricky to initially set up. The good news is that once they are set up and running, they are very easy to manage.

# Setting Up Python, Virtual Env, and your Python Environment

**This is actually the trickiest part of the whole workshop — once we get through this, the real fun begins!**

For this guide, I will be assuming you have a bash-type command line open. If you're on Windows, you should still be able to repeat most of these steps.

```bash
$ commands will be written like this
<variables> will be written with brackets
# eg
/home/<your name>/workspace
```

## Your Repo / Workspace

Fork the repo. Basically, what you'll be doing is making a personal copy on GitHub for you to be able to push changes to. The fork button looks like this when logged in (it's in the upper right):

![Forking the repo](../static/img/fork.png)

Copy / Clone your forked repo to a local workspace folder. It's a good idea to have a separate workspace folder set up for your dev projects.

```bash
$ cd ~/workspace
# Remember to change <your github name> to your github username
$ git clone git@github.com:<your github name>/lucky_flask.git
$ cd lucky_flask
```

## virtualenv & virtualenvwrapper

*Pay close attention here, this is the hard part.*

Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/). To do so, follow these steps (Caveat Empor: I haven't tried this on Windows):

### Linux & Mac OSX
```bash
$ sudo easy_install pip  # The command is different on windows
```

### Windows
```bash
python -m pip install -U pip
```

Then Follow [This Guide](https://github.com/davidmarble/virtualenvwrapper-win/)

### Linux  Mac OSX

```bash
$ pip install -U pip # yes, we're using pip to update pip
$ pip install virtualenvwrapper
```

### All OSes

```bash
# Here we set up our virtual environment
$ mkvirtualenv lucky
$ workon lucky
# Here we install python requirements
(lucky)$ pip install -r requirements # Note that '(lucky)' should now pop up
```

You will likely have issues for these steps. Just contact me and we'll work through them together. Remember, google is your friend.


# Testing it out

Did you get through that? Awesome. Now the fun really begins. Run this:

```bash
(lucky)$ cd apps/01_ketchup/
(lucky)$ python app.py
```

Then open your browser to http://localhost:5000/

☺
