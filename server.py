import os
import sys
from flask import Flask, render_template, request, send_from_directory, url_for, redirect, send_file, jsonify, flash
from example import Example
from methods import Methods
from notationReader import notationReader
from methodDrawer import methodDrawer
from methodPlayer import methodPlayer

# set up flask environment
app = Flask(__name__)
app.secret_key = 'dev'

@app.route("/")
def home():
    f = open("examples.txt")
    lines = f.readlines()
    methods = []
    for i in range(0, len(lines), 3):
        method = Methods(lines[i], lines[i+1], lines[i+2])
        methods.append(method)


    # songs = ["No Diggity", "Hypnotize", "99 Problems", "Party in the USA"]
    return render_template('form.html', methods=methods)

# accepts the post request from the website
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
            method = str(request.form['method'])
            flash("Please enter proper place and stage", "danger")
            return redirect(url_for("home"))
        # formattedString = changeRingingStringChecker(place, stage)
        # audioMaker(formattedString)
        # imageMaker(formattedString)
        print("Building example")

        formattedString = notationReader(place, stage)
        example = Example('audio/'+formattedString+'.wav', 'images/'+formattedString+'.jpg')

        methodPlayer(formattedString)
        methodDrawer(formattedString)
        return render_template('results.html', example=example, formattedString=formattedString)
    if request.method == 'GET':
        return "A get request to accept?!?"


# Retrieves images
@app.route('/images/<path:path>')
def send_image(path):
    print("Trying to send image" + path)
    return send_from_directory('images', path)

#retrieves audio files
@app.route('/audio/<path:path>')
def send_audio(path):
    print("Trying to send audio "+path)
    return send_from_directory('output_audio', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
