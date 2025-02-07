
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/stats", methods=["POST"])
def stats():
    sentence = request.form.get("sentence")
    words = sentence.split(' ')
    word_count = len(words)
    total = 0
    for word in words:
        total += len(word)
    char_count = total
    average = (total / len(words))
    return render_template("stats.html", word_count=word_count, char_count=char_count, average=average)


if __name__ == '__main__':
    app.run()

