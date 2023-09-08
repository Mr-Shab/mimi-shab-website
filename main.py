from flask import Flask
from flask import render_template
# create a flask application
app = Flask(__name__)


# register a route to the application
@app.route("/")
def hello_world():
  return render_template("home.html")


# check if it's a python script and run the app
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
