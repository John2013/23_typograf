from flask import Flask, render_template, jsonify, request, abort
from werkzeug.contrib.fixers import ProxyFix

import typograf as t

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/api/v1.0/perform', methods=["POST"])
def perform():
    if not request.json or 'text' not in request.json:
        abort(400)
    return jsonify({'result': t.perform(request.json['text'])}), 200


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run()
