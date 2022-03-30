#!/usr/bin/env python
import os
from flask import (Flask, jsonify, render_template, request, make_response,
                   send_from_directory)
from flask_cors import CORS
from db import get_full_name


app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    content_type = request.headers.get('Accept', '')
    browser = request.headers.get('User-Agent', '').lower()
    if request_wants_json():
        return jsonify(name=get_full_name())
    user_agent_prefixes = ("curl", "wget", "python")
    acceptable_types = ("text/plain", "", "*/*")
    is_cli_user_agent = (
        browser.startswith(user_agent_prefixes)
        and content_type in acceptable_types
    )
    if is_cli_user_agent:
        return make_response((u"{0}\n".format(get_full_name()), 200,
                              {'Content-Type': 'text/plain'}))
    else:
        return render_template('index.html', name=get_full_name())


@app.route('/humans.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


def request_wants_json():
    accepted = request.accept_mimetypes
    best = accepted.best_match(['application/json', 'text/html'])
    return (best == 'application/json' and
            accepted[best] > accepted['text/html'])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
