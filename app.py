from flask import Flask, render_template, results

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/stats", methods=["POST"])
def stats():
    sentence = results.form.get("sentence")
    words = sentence.split(' ')
    word_count = len(words)
    char_count = len(sentence)
    total = 0
    for word in words:
        total += len(word)
    average = (total / len(words))
    return render_template("stats.html", word_count=word_count, char_count=char_count, average=average)


if __name__ == '__main__':
    app.run()
