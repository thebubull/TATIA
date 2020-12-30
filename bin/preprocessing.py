import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

from bin.constants import categories, display_percent


def summary_transform(summary):
    # 1 - Lowercase
    summary = summary.lower()

    # 2 - Remove Punctuation
    summary = "".join([char for char in summary if char not in string.punctuation])

    # 3 - Tokenization
    tokens = word_tokenize(summary)

    # 4 - Stopword Filtering
    stop_words = stopwords.words('english')
    words = [word for word in tokens if word not in stop_words]

    # 5 - Stemming
    porter = PorterStemmer()
    return [porter.stem(word) for word in words]


def preprocess_file(in_path, out_path):
    data = pd.read_csv(in_path, encoding="utf-8")
    count = len(data.index) - 1
    processed_list = []

    for index, row in data.iterrows():
        obj = {
            "words": summary_transform(row[6]),
        }
        for category in categories:
            obj[category] = "1" if category in row[5] else "0"

        processed_list.append(obj)
        display_percent(index, count, 'Preprocessing ')

    out = pd.DataFrame(processed_list)
    out.to_csv(out_path, encoding='utf-8')


def preprocess_train(path="../data/data-grouped.csv"):
    preprocess_file(in_path=path, out_path='../data/dataSet-Train.csv')

