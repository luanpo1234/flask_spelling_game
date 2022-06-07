"""
Set-ExecutionPolicy Unrestricted -Scope Process
venv/Scripts/activate.ps1
"""
from flask import Flask, redirect, url_for, render_template, request, session
import random
import bee
import string

TEST_LETTER_SPEC = ("smarted", "r") #Sample letter list and special letter for testing.
WORDS_7 = bee.WORDS_7
WORDLIST = bee.WORDLIST
LETTER_LIST, SPECIAL_LETTER = bee.get_letters(WORDS_7)
LETTERS_STR = f"{bee.to_str(LETTER_LIST)} <br /> Mandatory letter: {SPECIAL_LETTER.upper()}"
SOLUTIONS = bee.get_solutions(WORDLIST, LETTER_LIST, SPECIAL_LETTER)
SOLVE = False

app = Flask(__name__)
app.secret_key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))


def build_list_used_str(lst, class_="column-list", sort=True):
    if len(lst) == 0:
        return ""
    res = f"<h5>You have found {len(lst)} words.</h5> <ul class= {class_}>"
    if sort:
        lst = sorted(lst)
    for el in lst:
        res = res + "<li>" + el + "</li>"
    res += "</ul>"
    return res

@app.route("/")
def home():
    return render_template("index.html", letters=LETTERS_STR)

@app.route("/", methods=["POST", "GET"])
def check_word():
    if request.method == "POST":
        session.permanent = False    
        msg = ""
        word = request.form["wordInput"].lower()
        if SOLVE == True:
            session["used_words"] = SOLUTIONS
            points = 0
            for w in SOLUTIONS:
                points += bee.check_score(w, WORDLIST, LETTER_LIST, SPECIAL_LETTER)[1]
            session["total_score"] = points
        else:
            if "used_words" not in session:
                session["used_words"] = []
            if "total_score" not in session:
                session["total_score"] = 0
            msg, points = bee.check_score(word, WORDLIST, LETTER_LIST, SPECIAL_LETTER)
            if points != 0:
                if word in session["used_words"]:
                    msg = "Word already has been used!"
                else:
                    session["used_words"].append(word)
                    session["total_score"] += points
        letters = LETTERS_STR
        msg_score = f"Total score: {session['total_score']} <br /> {msg} <br />" 
        list_used_html = build_list_used_str(session["used_words"])
        print(SPECIAL_LETTER)
        if set(session["used_words"]) == set(SOLUTIONS):
            return render_template("solved.html", letters=letters, msgscore=msg_score, listused=list_used_html)
    return render_template("index.html", letters=letters, msgscore=msg_score, listused=list_used_html)

if __name__ == "__main__":
    print(SOLUTIONS)
    app.run(port=5000, debug=True)