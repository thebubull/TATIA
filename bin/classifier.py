from ast import literal_eval

import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MultiLabelBinarizer

clf = None
mlb = MultiLabelBinarizer()


def train(path='../data/dataSet-Train.csv'):
    global clf, mlb
    data = pd.read_csv(path, encoding="utf-8")
    data['genres'] = data['genres'].apply(literal_eval)

    train, test = model_selection.train_test_split(data, test_size=0.2, random_state=42)
    X_train = train.words
    Y_train_text = train.genres
    X_test = test.words
    Y_test_text = test.genres

    Y_train = mlb.fit_transform(Y_train_text)
    Y_test = mlb.transform(Y_test_text)

    # Pipeline
    clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', OneVsRestClassifier(SGDClassifier())),
    ])

    clf.fit(X_train, Y_train)
    predicted = clf.predict(X_test)
    accuracy = np.mean(predicted == Y_test)
    print("Accuracy : {}".format(accuracy))


def predict(summaries):
    global clf, mlb
    if clf is None:
        raise Exception("Untrained Neural Network")

    predictions = clf.predict(summaries)
    return mlb.inverse_transform(predictions)
