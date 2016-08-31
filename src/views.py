from src import app
from flask import render_template, send_file, jsonify

@app.route('/')
def index():
	return 'Hello World!'