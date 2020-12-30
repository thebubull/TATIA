import pandas as pd

from bin.classifier import train, predict
from bin.constants import display_percent
from bin.preprocessing import preprocess_train, summary_transform

print('Preprocessing Train...')
preprocess_train()
print('\rPreprocess Train finished.               ')
print('Training...')
train()
print('\rTrain finished.')


def classify_summary(summary):
    print(predict(summary))


def classify_file(path):
    data = pd.read_csv(path, encoding="utf-8")
    size = len(data.index) - 1

    processed_list = []
    for index, row in data.iterrows():
        prediction = predict(summary_transform(row[6]))
        processed_list.append({
            "title": row[2],
            "genres": prediction
        })

        display_percent(index, size, 'Prediction ')

    out = pd.DataFrame(processed_list)
    out.to_csv('../out.csv', encoding='utf-8')


classify_file('../data/data-test-copy.csv')
