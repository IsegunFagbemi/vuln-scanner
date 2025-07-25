from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    response = Response("Hello from Vulnerable Test Site!")
    return response

if __name__ == '__main__':
    app.run(port=5000)