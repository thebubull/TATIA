import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import sys


data = pd.read_csv("../data/data-grouped.csv", encoding="utf-8")
count = len(data.index)
out_list = []


def display_percent(i):
    current_percent = i * 100 / count
    sys.stdout.write("\r")
    sys.stdout.write("[%-20s] %d%%" % ('='*int(current_percent/5), current_percent))
    sys.stdout.flush()


for index, row in data.iterrows():
    summary = row[6]

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
    stems = [porter.stem(word) for word in words]
    #print(tokens)

    out_list.append({
        "words": stems,
        "genre": row[5].split(';')
    })
    display_percent(index)

out = pd.DataFrame(out_list)
out.to_csv('../data/dataSet-Train.csv', encoding='utf-8')
