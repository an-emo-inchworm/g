from flask import Flask, request, jsonify

app = Flask(__name__)

# Checking if Flask server is running
@app.route('/')
def home():
    return "Flask server is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

