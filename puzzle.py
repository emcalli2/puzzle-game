from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

WORDS = ["banana", "python", "cloud", "server", "flask", "google", "puzzle"]
SECRET_WORD = random.choice(WORDS)
SCRAMBLED = ''.join(random.sample(SECRET_WORD, len(SECRET_WORD)))

HTML = """
<!DOCTYPE html>
<html>
<head><title>Puzzle Game</title></head>
<body>
    <h1>Unscramble This Word:</h1>
    <h2>{{ scrambled }}</h2>

    <form method="post">
        <input name="guess" placeholder="Your guess here" autofocus>
        <input type="submit" value="Guess">
    </form>

    {% if result %}
        <p><strong>{{ result }}</strong></p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def puzzle():
    guess = request.form.get("guess", "").lower()
    result = ""
    if guess:
        if guess == SECRET_WORD:
            result = "🎉 Correct! You win!"
        else:
            result = "❌ Nope! Try again."
    return render_template_string(HTML, scrambled=SCRAMBLED, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
