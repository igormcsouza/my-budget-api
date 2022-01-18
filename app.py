from flask import Flask
from project.infrastructure.database import main
from flask_migrate import Migrate

app = Flask(__name__)
db = main.init_app()

# migrate = Migrate(app, db)

@app.route("/", methods=["GET"])
def test2():
    return "<p>app test</p>"
