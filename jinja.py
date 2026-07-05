### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine


### Jinja2 Templae Engine
"""
{{ }} expressions to print output in  html
{%...%} conditional statements . for loops
{#...#} this is for comments

"""

from flask import Flask,render_template,request,redirect,url_for


# redirect,url_for used for Building Url Dynamically
"""
It creates and instance of the class, which will be your WSGI (Web serve gateway Interface ) application.

"""


app=Flask(__name__)


@app.route("/")
def welcome():
        return "<html><h1>Welcome to this  Flask Course.</h1></html>"


@app.route("/index",methods=["GET"])
def index():
        return render_template("index.html")
@app.route("/about")
def about():
        return render_template("about.html")




@app.route("/submit",methods=["GET","POST"])
def submit():
        if request.method=="POST":
            name= request.form["name"]
            return f"Hello {name}"
        else:
            return render_template("form.html")

## Variable Rule
@app.route("/success/<int:score>")
def success(score):
        res=""
        if score>=50:
              res="PASS"
        else:
              res="FAIL"
        return render_template("result.html",results=res)


@app.route("/successres/<int:score>")
def success1(score):
        res=""
        if score>=50:
              res="PASS"
        else:
              res="FAIL"
        
        exp = {"score":score,"res":res}
        return render_template("result1.html",results=exp)




## If condition Rule
@app.route("/successif/<int:score>")
def success2(score):
        return render_template("result.html",results=score)

@app.route("/fail/<int:score>")
def fail(score):
        return render_template("result.html",results=score)




if __name__=="__main__":
        app.run(debug=True)
