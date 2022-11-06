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

# Pre SSH Key and GPG Signing Setup

Note: One thing to keep in mind is that GitHub requires the email on your key and in your Git config to match your GitHub email address. To set that in Git, use: ```git config --global user.email "YOUR@EMAIL.com"``` - use the usrs.noreply.github.com email address instead of your real for SSH Key and GPG generation and commit emails if you want your email to remain private.

Unlike when setting your commit email address, it is necessary to use the full noreply email address that GitHub provides. You can find it under the "Keep my email addresses private" section on the [GitHub email settings page](https://github.com/settings/emails). This email address should look something like:

```XXXXXXXX+USERNAME@users.noreply.github.com```

Use this email address to generate your GPG key instead of simply using "USERNAME@users.noreply.github.com."

# SSH Key Setup
[Github Instructions Here](https://docs.github.com/articles/generating-an-ssh-key/)

Add SSH Key to the ssh agent for automatically using key for push via ssh:

```ssh-add ~/.ssh/<yourkey>``

Start ssh-agent:

``` eval `ssh-agent -s` ```

To remove SSH keys from the ssh-agent if you ever need to:

```ssh-add -D ~/.ssh/<yourkey>```

Testing ssh connection to git using ssh key:

```ssh -T git@github.com```

# GPG signing
[Github Instructions Here](https://docs.github.com/articles/generating-a-gpg-key/)

Settings after gpg is generated:

```git config commit.gpgsign true```

Then, get the ID of your GPG key: ```gpg --list-secret-keys --keyid-format LONG.```

Add that ID from above to your Git config: ```git config --local user.signingkey "[GPG_KEY]"```, (Make sure to replace “GPG_KEY” with the ID from your GPG key in the previous command)

Awesome! Now that the project is configured to use GPG keys to sign code, I can commit code like normal, e.g. ```git commit -m "Changed x code to y"```.

# Changing Remote URL to SSH URL

```git remote set-url origin "git@github.com:hrmmmwhynot/hangman_web.git"```
