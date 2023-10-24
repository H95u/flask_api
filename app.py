from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

try:
    from controller import *
except Exception as e:
    print(e)

if __name__ == 'main':
    app.run(host="0.0.0.0", port=5000)
