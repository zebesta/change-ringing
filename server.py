from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    songs = ["No Diggity", "Hypnotize", "99 Problems", "Party in the USA"]
    return render_template('form.html', songs=songs)

@app.route("/accept")
def accept():
    return "You submitted the form!!!"

@app.route("/examples")
def examples():
    return render_template('examples.html')

if __name__ == "__main__":
    app.run()
