from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test2():
    return "<p>app test</p>"
