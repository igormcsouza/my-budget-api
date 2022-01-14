from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test():
    return "<p>app test</p>"