# app.py

from flask import Flask, render_template, request
import number_guessing  # Import the game logic from number_guessing.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Start a new game if it's the first time visiting the page
    if 'target' not in request.cookies:
        target = number_guessing.generate_number()  # Call the function from number_guessing.py
        response = render_template('number_guessing.html', message="Guess the number between 1 and 100", guess=None)
        response.set_cookie('target', str(target))  # Set the target number in cookies
        return response

    target = int(request.cookies.get('target'))
    message = ""
    guess = None

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])  # Get the guess from the form
            if guess < target:
                message = "Too low! Try again."
            elif guess > target:
                message = "Too high! Try again."
            else:
                message = "Congratulations! You guessed it right."
        except ValueError:
            message = "Please enter a valid number."  # Handle invalid input

    return render_template('number_guessing.html', message=message, guess=guess)

if __name__ == '__main__':
    app.run(debug=True)
