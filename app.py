from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

try:
    from controller import *
except Exception as e:
    print(e)

if __name__ == '__main__':
    app.run()
