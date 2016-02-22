from flask import Flask

# Initialize the flask
app = Flask(__name__)


# The index path
@app.route('/')
def index(): pass


# Only run if from an application context
if __name__ == "__main__":
    app.run()
