from flask import Flask, render_template, request

app = Flask(__name__)

import random
secret_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    guess = None
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            if guess < secret_number:
                message = "Too low! Try again."
            elif guess > secret_number:
                message = "Too high! Try again."
            else:
                message = "Congratulations! You guessed the number."
        except ValueError:
            message = "Please enter a valid number."
    
    return render_template("index.html", message=message, guess=guess)

if __name__ == "__main__":
    app.run(debug=True)
