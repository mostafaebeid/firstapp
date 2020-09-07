# Import library Flask from package flask
from flask import Flask

#Create a Flask object
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
