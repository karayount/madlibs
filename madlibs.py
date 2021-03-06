from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet', methods=["POST"])
def greet_person():
    """Greet user."""

    player = request.form.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_game_form():
    """Render Goodbye or, if the player wishes to play a game, ask madlibs game questions."""

    response = request.args.get("playgame")

    if response == "no":
        return render_template("goodbye.html")
    elif response == "yes":
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():

    person_response = request.args.get("person")
    color_response = request.args.get("color")
    noun_response = request.args.get("noun")
    adjective_response = request.args.get("adjective")
    other_adjective_response = request.args.get("other_adjective")
    adverb_response = request.args.getlist("adverb")

    which_story = choice(["madlib.html", "meglib.html"])

    return render_template(which_story,
                       person=person_response,
                       color=color_response,
                       noun=noun_response,
                       adjective=adjective_response,
                       other_adjective=other_adjective_response,
                       adverb=choice(adverb_response))
    

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
