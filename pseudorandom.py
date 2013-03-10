#!/usr/bin/env python
import os
from flask import Flask, render_template, request
from names import get_full_name


app = Flask(__name__)


@app.route("/")
def index():
    if request.headers.get('User-Agent', '')[:4].lower() == 'curl':
        return u"{0}\n".format(get_full_name())
    else:
        return render_template('index.html', name=get_full_name())


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
