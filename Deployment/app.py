import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
with open("model.pkl", "rb") as f:
    getstocks = pickle.load(f, encoding='utf8')

# model = pickle.load(open('model.pkl', encoding='latin1'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    return render_template('index.html', prediction_text='The tickers our AI has chosen are:\n {}'.format(getstocks))


if __name__ == "__main__":
    app.run(debug=False)