import flask
import pickle
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

with open(f'model/model_random-forest.pkl','rb') as f:
	model = pickle.load(f)

with open(f'model/preprocessed_word/bow_feature.pkl','rb') as f:
	bow = joblib.load(f)

def dummy_fun(doc):
	return doc

vectorizer = CountVectorizer(max_features=4000,preprocessor=dummy_fun, tokenizer=dummy_fun, vocabulary=bow['vocabulary'])

app = flask.Flask(__name__, template_folder= 'templates')
@app.route('/', methods=['GET', 'POST'])
def main():
	if flask.request.method == 'GET':
		return (flask.render_template('main_page.html'))

	if flask.request.method == 'POST':
		review = flask.request.form['comment_review']
		comment_text = "comment review is:"
		if (model.predict(vectorizer.transform([list(review.split(" "))]))==1):
			prediction = "This is spam comment"
		else:
			prediction = "its Ham, suited comment for music videos"

		return(flask.render_template("main_page.html" ,comment_text=comment_text ,result=prediction))


if __name__ == '__main__':
	app.run()



