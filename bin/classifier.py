# FROM https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#training-a-classifier
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

data = pd.read_csv('../data/dataSet-Train.csv', encoding="utf-8")

X_train, X_test, y_train, y_test = model_selection.train_test_split(data['words'], data['genre'], test_size=0.2)

# Building a pipeline
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier()),
])


text_clf = text_clf.fit(X_train, y_train)

# Evaluation of the performance on the test set
predicted = text_clf.predict(X_test)

accuracy = np.mean(predicted == y_test)

print("Accuracy : ", accuracy)
