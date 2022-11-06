import functools
import requests
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('hangman', __name__, url_prefix='/')
WORD_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"
GAME_OVER_WRONGS = 6

def get_word():
    r = random.randint(1,10000)
    response = requests.get(WORD_SITE)

    return response.content.splitlines()[r].decode("utf-8")


def check_word(word: str, user_input: str, user_current: str):
    s = ""
    for i in range(len(word)):
        if user_input == word[i] or user_current[i] == word[i]:
            s += f"{word[i]}"
        else:
            s += "_"

    return s


def initial_blanks(word: str):
    s = ""
    for c in word:
        s += "_"

    return s


def print_with_space(word: str):
    s = ""
    for c in word:
        s += f"{c} "

    return s


def print_hangman(stage: int):
    hangman0 = "|\n"
    hangman1 = "O\n"
    hangman2 = "|\n"
    hangman3 = "/|\n"
    hangman4 = "/|\\\n"
    hangman5 = "/   \n"
    hangman6 = "/ \\\n"
    hangman_current = hangman0

    match stage:
        case 0:
            hangman_current = hangman0
        case 1:
            hangman_current = hangman0 + hangman1
        case 2:
            hangman_current = hangman0 + hangman1 + hangman2
        case 3:
            hangman_current = hangman0 + hangman1 + hangman3
        case 4:
            hangman_current = hangman0 + hangman1 + hangman4
        case 5:
            hangman_current = hangman0 + hangman1 + hangman4 + hangman5
        case 6:
            hangman_current = hangman0 + hangman1 + hangman4 + hangman6
        case _:
            hangman_current = "Something went wrong!\n"
    
    return hangman_current


def check_win(user_word: str, word: str) -> bool:
    if user_word == word:
        # print("\n You Win!!!")
        return True

    return False


def check_lose(max_wrongs: int, user_wrongs: int) -> bool:
    if max_wrongs == user_wrongs:
        # print("\n You Lose!!!")
        return True

    return False


@bp.route('/', methods=('GET', 'POST'))
def index():
    post = {}
    post['word'] = get_word()
    post['letter'] = ""
    post['user_wrongs'] = 0
    post['user_current'] = initial_blanks(post['word'])
    post['winlose'] = ""
    post['wordlength'] = len(post['word'])

    if request.method == 'POST':
        post['word'] = request.form['word']
        post['letter'] = request.form['letter']
        post['user_current'] = request.form['user_current']
        post['user_wrongs'] = int(request.form['user_wrongs'])
        post['winlose'] = request.form['winlose']
        post['wordlength'] = request.form['wordlength']

        if not post['letter']:
            error = 'Letter is empty. Please input a letter.'
            flash(error)

        if post['letter'] not in post['word']:
            post['user_wrongs'] += 1
        
        post['user_current'] = check_word(post['word'], post['letter'], post['user_current'])

    if (check_win(post['user_current'], post['word']) == True):
        post['winlose'] = "You Win!!!"

    if (check_lose(GAME_OVER_WRONGS, post['user_wrongs']) == True):
        post['winlose'] = "You Lose!!!"

    post['hangman'] = print_hangman(post['user_wrongs'])

    return render_template('main/main.html', post=post)