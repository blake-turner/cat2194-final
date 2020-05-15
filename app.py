#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/stay_at_home")
def stay_at_home():
    return render_template("quarantine activities.html")

#start the server
if __name__ == "__main__":
    app.run()
    

