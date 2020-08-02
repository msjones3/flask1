from flask import *
app = Flask(__name__)

@app.route("/")
def main():
    myName = 'Cheryl'
    return f"Hello, {myName}!"

app.run(debug=True)