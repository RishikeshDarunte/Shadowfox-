from flask import Flask, render_template, request, redirect, url_for, session
import random
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key
# Predefined list of words
word_list = ["hangman", "python", "programming", "openai", "computer", "science"]
def choose_word():
    """Function to choose a random word from the list."""
    return random.choice(word_list)
def initialize_game():
    """Initialize or reset the game session."""
    session['word'] = choose_word()
    session['guessed_letters'] = []
    session['incorrect_guesses'] = 0
    session['max_attempts'] = 6
    session['game_over'] = False
    session['message'] = None
@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle the main game logic and rendering."""
    if 'word' not in session:
        initialize_game()
    if session.get('game_over'):
        return render_template('index.html', 
                               display_word=" ".join([letter if letter in session['guessed_letters'] else "_" for letter in session['word']]), 
                               incorrect_guesses=session['incorrect_guesses'], 
                               max_attempts=session['max_attempts'],
                               message=session.get('message'))
    if request.method == 'POST':
        guess = request.form.get('guess', '').lower()
        if not guess.isalpha() or len(guess) != 1:
            session['message'] = "Invalid input. Please enter a single letter."
        elif guess in session['guessed_letters']:
            session['message'] = "You've already guessed that letter."
        else:
            session['guessed_letters'].append(guess)
            if guess in session['word']:
                if all(letter in session['guessed_letters'] for letter in session['word']):
                    session['message'] = f"Congratulations! You've guessed the word: '{session['word']}'"
                    session['game_over'] = True  # End the game
                else:
                    session['message'] = None
            else:
                session['incorrect_guesses'] += 1
                if session['incorrect_guesses'] >= session['max_attempts']:
                    session['message'] = f"You have lost! The word was '{session['word']}'."
                    session['game_over'] = True  # End the game
    display_word = " ".join([letter if letter in session['guessed_letters'] else "_" for letter in session['word']])
    return render_template('index.html', 
                           display_word=display_word, 
                           incorrect_guesses=session['incorrect_guesses'], 
                           max_attempts=session['max_attempts'],
                           message=session.get('message'))
@app.route('/reset')
def reset_game():
    """Reset the game session."""
    session.clear()
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)