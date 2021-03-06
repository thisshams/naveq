from flask import Flask, render_template, request, url_for
from response import get_response

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/selectFromMapCurrent')
def selectFromMapCurrent():
    return render_template('selectFromMapCurrent.html')


@app.route('/selectFromMapDestination')
def selectFromMapDestination():
    return render_template('selectFromMapDestination.html')


@app.route('/firstFloorMap')
def firstFloorMap():
    return render_template('firstFloorMap.html')


@app.route('/groundFloorMap')
def groundFloorMap():
    return render_template('groundFloorMap.html')


@app.route('/toMap')
def toMap():
    return render_template('toMap.html')


@app.route('/firstFloorTouchMap')
def firstFloorTouchMap():
    return render_template('firstFloorTouchMap.html')


@app.route('/groundFloorTouchMap')
def groundFloorTouchMap():
    return render_template('groundFloorTouchMap.html')


@app.route('/bothMaps')
def bothMaps():
    return render_template('bothMaps.html')


@app.route("/get")
# function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    chat = get_response(userText)
    return chat


if __name__ == "__main__":
    app.run(debug=True)
