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
```
