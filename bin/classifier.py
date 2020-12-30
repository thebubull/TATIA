import pandas as pd
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline

data = pd.read_csv('../data/dataSet-Train.csv', encoding="utf-8")
categories = ["Biography", "Comedy", "Detective Fiction", "Drama", "Fantasy", "Fiction", "Horror", "Nonfiction", "Romance", "Science Fiction", "Thriller"]

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

