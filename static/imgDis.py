from flask import Flask, url_for, abort
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Napier"

@app.route('/static-example/img')
def static_example_img():
  start = '<img src="'
  url = url_for('static', filename='vamsk.jpg')
  end = '">'
  return start+url+end, 200

if __name__ == "__main__":

  app.run(host='0.0.0.0', debug=True)
