from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


def test_response():
    response = app.test_client().get("/")
    assert response.status_code == 200
