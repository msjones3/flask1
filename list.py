from flask import *
app = Flask(__name__)

@app.route("/")
def main():
    myList = ['eggs', 'bread', 'milk', 'flour']
    return f"{myList}"

app.run(debug=True)