import os
from flask import Flask, render_template
from names import get_full_name


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', name=get_full_name())


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
