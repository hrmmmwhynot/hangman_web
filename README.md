# hangman_web
hangman_webapp

# Devlopment guidelines
Generally, the following order is the most appropriated.

```$ git clone <Project A>  # Cloning project repository```

```$ cd <Project A> # Enter to project directory```

```$ python3 -m venv venv # If not created, creating virtualenv```

```$ source ./my_venv/bin/activate # Activating virtualenv```

```(my_venv)$ pip3 install -r ./requirements.txt # Installing dependencies```

```(my_venv)$ deactivate # When you want to leave virtual environment```

# Configure VSCode as git core editor

```git config --global core.editor 'code --wait'```

# GPG signing by default

```git config commit.gpgsign true```