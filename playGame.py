#import os
import time
import flask
import hangmanWords

newGame = True
gameOver = False
word = ""
blanks = ""
lives = 8
guesses = []

app = flask.Flask(__name__)
app.secret_key = " "

@app.route('/') 
def index():
    global newGame
    global gameOver
    global lives
    global word
    global blanks
    global guesses

    newGame = True
    word = ""
    blanks = ""
    lives = 8
    gameOver = False
    guesses = []
            
    return flask.render_template("main.html")

@app.route('/play', methods = ['GET', 'POST']) 
def game():
    global newGame
    global gameOver
    global lives
    global word
    global blanks
    global guesses
    
    if newGame:
        guesses = []
        word = (hangmanWords.getRandomWord()).lower()
        print(word)
        blanks = hangmanWords.wordtoBlanks(word)

    if gameOver:
        pass
    else:
        pageBlank = hangmanWords.printwordBlanks(blanks)
        newGame = False

    guess = flask.request.form.get("guess", "")
    #print(guess)
    
    if guess in guesses:
        message = "Letter " + guess + " already used"
        flask.flash(message)
    else:
        guesses.append(guess)
    #print(guesses)
    
    if guess in word:
        blanks = hangmanWords.updateLetters(guess, word, blanks)
        pageBlank = hangmanWords.printwordBlanks(blanks)
        #print(word)
        #print(pageBlank)
    else:
        lives = lives - 1
        #print(lives)
        message = "LIVES LEFT : " + str(lives)
        flask.flash(message)
        if lives == 0:
            gameOver =  True
            flask.flash("YOU LOSE!!")
            flask.flash(flask.Markup("<a href = '/'> RESTART </a>"))

    if '_' not in blanks and gameOver == False:
        gameOver =  True
        flask.flash("YOU WIN!!")
        flask.flash(flask.Markup("<a href = '/'> RESTART </a>"))
        
    return flask.render_template("playGame.html", blank = pageBlank)


#port = int(os.environ.get('PORT', 10000))
#app.run(host = "0.0.0.0", port = port)
app.run(debug = True)
