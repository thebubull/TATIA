import string
import sys

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize


def display_percent(current, total, prefix=""):
    current_percent = current * 100 / total
    sys.stdout.write("\r")
    sys.stdout.write("%s[%-20s] %d%%" % (prefix, '='*int(current_percent/5), current_percent))
    sys.stdout.flush()


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
    stem_sentence = ""
    for word in words:
        stem = porter.stem(word)
        stem_sentence += stem
        stem_sentence += " "
    stem_sentence = stem_sentence.strip()
    return stem_sentence


def preprocess_file(in_path, out_path):
    data = pd.read_csv(in_path, encoding="utf-8")
    count = len(data.index) - 1
    processed_list = []

    for index, row in data.iterrows():
        obj = {
            "words": summary_transform(row[6]),
            "genres": row[5].split(";")
        }

        processed_list.append(obj)
        display_percent(index, count, 'Preprocessing ')

    out = pd.DataFrame(processed_list)
    out.to_csv(out_path, encoding='utf-8')


def preprocess_train(path="../data/data-grouped.csv"):
    preprocess_file(in_path=path, out_path='../data/dataSet-Train.csv')

