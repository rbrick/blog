from flask import Flask
from flask import render_template

# Initialize the flask
app = Flask(__name__)


# The index path
@app.route('/')
def index():
    return render_template('base.html')


# Only run if from an application context
if __name__ == "__main__":
    app.run()
