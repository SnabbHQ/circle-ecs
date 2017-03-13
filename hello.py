from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! This is CD live baby!'

if __name__ == "__main__":
    app.run()
