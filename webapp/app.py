import flask
import pickle
import pandas as pd

with open(f'model/random_forest.pkl','rb') as f:
	model = pickle.load(f)

with open(f'model/vectorizer.pkl') as f:
	vectorizer = pickel.load(f)

app = flask.Flask(__name__, template_folder= 'templates')

@app.route('/', methods=['GET', 'POST'])

def main():
	if flask.request.method == 'GET':
		return (flask.render_template('main_page.html'))

	if flask.request.method == 'POST':
		
		review = flask.request.form['comment_review']
		predict_text = "comment review is:"
		prediction = model.predict(vectorizer.transform([review]))
		return(flask.render_template("main_page.html" ,predict_text=predict_text ,result=prediction))


if name == '__main__':
	app.run()

