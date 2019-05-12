from flask import Flask, redirect
import pickle
import random

app = Flask(__name__)
with open('links.txt', 'rb') as db:
	array = pickle.load(db)

@app.route('/')
def redir():
	return redirect(random.choice(array))

if __name__ == '__main__':
	app.run()
