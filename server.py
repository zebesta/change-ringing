from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    songs = ["No Diggity", "Hypnotize", "99 Problems", "Party in the USA"]
    return render_template('form.html', songs=songs)

@app.route("/accept", methods=['POST', 'GET'])
def accept():
    if request.method == 'POST':
        print("HALP!!")
        if 'change' not in request.form:
            return "No change in the input!"
        change = str(request.form['change'])
        if len(change) < 1:
            song = str(request.form['song'])
            return "No string selected, looking at song: " + song

        return "You submitted the form!!! With change: " + change
    if request.method == 'GET':
        return "A get request to accept?!?"


@app.route("/examples")
def examples():
    return render_template('examples.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
