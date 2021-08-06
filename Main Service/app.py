import os
from flask import Flask, request, send_from_directory, Response
from flask_cors import CORS

import json

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/', defaults=dict(filename=None))
@app.route('/<filename>', methods=['GET'])
def index(filename):
    print(filename)
    filename = filename or 'index.html'
    return send_from_directory('/frontend/', filename)


@app.route('/<path:dir1>/<path:filename>', methods=['GET'])
def index2(dir1, filename):
    filename = filename or 'index.html'
    return send_from_directory(os.path.join('/frontend', dir1), filename)


@app.route('/<path:dir1>/<path:dir2>/<path:filename>', methods=['GET'])
def index3(dir1, dir2, filename):
    filename = filename or 'index.html'
    return send_from_directory(os.path.join('/frontend', dir1, dir2), filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)