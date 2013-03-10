#!/usr/bin/env python
import os
from flask import (Flask, render_template, request, make_response,
                   send_from_directory)
from names import get_full_name


app = Flask(__name__)


@app.route("/")
def index():
    content_type = request.headers.get('Content-Type', '')
    browser = request.headers.get('User-Agent', '').lower()
    if browser[:4] in ('curl', 'wget') and content_type in ('text/plain', ''):
        return make_response((u"{0}\n".format(get_full_name()), 200,
                              {'Content-Type': 'text/plain'}))
    else:
        return render_template('index.html', name=get_full_name())


@app.route('/humans.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
