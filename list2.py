from flask import *
app = Flask(__name__)

@app.route("/")
def main():
    myList = ['eggs', 'bread', 'milk', 'flour']
    return render_template('list.html', myList=myList)

app.run(debug=True)