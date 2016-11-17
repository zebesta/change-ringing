from flask import Flask, render_template, request
app = Flask(__name__)
from example import Example

@app.route("/")
def home():
    songs = ["No Diggity", "Hypnotize", "99 Problems", "Party in the USA"]
    return render_template('form.html', songs=songs)

@app.route("/accept", methods=['POST', 'GET'])
def accept():
    if request.method == 'POST':
        print("HALP!!")
        if 'place' not in request.form:
            return "No place in the input!"
        if 'stage' not in request.form:
            return "No stage in the input!"
        place = str(request.form['place'])
        stage = str(request.form['stage'])
        if ((len(place) < 1) or (len(stage) < 1)):
            song = str(request.form['song'])
            return "No string selected, looking at song: " + song
        formattedString = changeRingingStringChecker(place, stage)
        # audioMaker(formattedString)
        # imageMaker(formattedString)
        print("Building example")
        example = Example('out.jpg', 'out.wav')
        return render_template('results.html', example)
        return "You submitted the form!!! With place: " + place + " and stage: " + stage
    if request.method == 'GET':
        return "A get request to accept?!?"


@app.route("/examples")
def examples():
    return render_template('examples.html')

# Retrieves images
@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

#retrieves audio files
@app.route('/audio/<path:path>')
def send_js(path):
    return send_from_directory('audio', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
