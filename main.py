from flask import Flask
from flask import render_template, jsonify

# create a flask application
app = Flask(__name__)

JOBS = [
  {
    "id": "1",
    "title": "Data Scientist",
    "location": "Enugu, Nigeria",
    "salary": "#250,000"
  },

  {
    "id": "2",
    "title": "Data Analyst",
    "location": "Los Angele, California, U.S.A.",
    "salary": "$17,000"
  },

  {
    "id": "3",
    "title": "Python Developer",
    "location": "Lagos, Nigeria",

  },

  {
    "id": "4",
    "title": "Web Developer",
    "location": "Remote",
    "salary": "#1,000,000"
  },
  
]

# register a route to the application
@app.route("/")
def hello_world():
  return render_template("home.html", jobs = JOBS, company_name = "Shab-Tech")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

# check if it's a python script and run the app
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
