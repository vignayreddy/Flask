from flask import Flask


"""

It creates and instance of the class, which will be your WSGI (Web serve gateway Interface ) application.

"""


app=Flask(__name__)


@app.route("/")
def welcome():
        return "Welcome to this  Flask Course. This should be an amazing course"


@app.route("/index")
def index():
        return "Welcome to the index page"

if __name__=="__main__":
        app.run(debug=True)
