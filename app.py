from flask import Flask

app = Flask(__name__)

@app.route('/')
<<<<<<< HEAD
def hello():
    return "Hello World from Moin Tabani!"
=======
def hello_world():
    return 'Hello World from Moin Tabani!'
>>>>>>> d1484daed985c543d0207377fdc83439cafdf053

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Make sure it's accessible from outside

