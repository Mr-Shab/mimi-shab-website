from flask import Flask
# create a flask application
app = Flask(__name__)


# register a route to the application
@app.route("/")
def hello_world():
  return "Hello world"


# check if it's a python script and run the app
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
