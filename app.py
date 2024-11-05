
from flask import Flask, request, jsonify, send_from_directory
import os
app = Flask(__name__)

@app.route('/')

def home():
    return send_from_directory(os.getcwd(), 'index.html')


if __name__ == '__main__':
    app.run(debug=True)