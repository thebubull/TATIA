import pandas as pd
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline

from bin.constants import categories

text_clf = None


def train(path='../data/dataSet-Train.csv', printAccuracy=False):
    global text_clf
    data = pd.read_csv(path, encoding="utf-8")

    train, test = model_selection.train_test_split(data, test_size=0.2, random_state=42)
    X_train = train.words
    X_test = test.words


    # Building a pipeline
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', OneVsRestClassifier(SGDClassifier())),
    ])

    for category in categories:
        print(category)
        text_clf = text_clf.fit(X_train, train[category])

        # Evaluation of the performance on the test set
        predicted = text_clf.predict(X_test)

        print("Accuracy : {}".format(accuracy_score(test[category], predicted)))


def predict(summaries):
    global text_clf
    if text_clf is None:
        raise Exception("Untrained Neural Network")
    predicted = {}
    for category in categories:
        predicted[category] = text_clf.predict(summaries)
    return predicted
