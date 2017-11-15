import ConfigParser
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html'), 200
