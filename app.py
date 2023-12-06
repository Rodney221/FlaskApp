from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="template")
 
@app.route('/')
def genius():
   return '<h1>Hello, Genius</h1>'

@app.route('/about/')
def about():
	return '<h3>It feels great to be a genius!</h3>'

