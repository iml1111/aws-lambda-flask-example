from flask import Flask

application = Flask(__name__)


@application.route('/')
def index():
	return """
	<h1>AWS-Lambda-Flask-Example</h1>
	<p>HI,  I'M IML!</p>
	"""


@application.route("/add/<int:a>/<int:b>")
def add_api(a, b):
	return {"msg": "success", "result": a + b}, 200


if __name__ == '__main__':
	application.run(debug=True)