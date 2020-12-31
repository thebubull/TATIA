import pandas as pd

from classifier import train, predict
from preprocessing import preprocess_train

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

    predicted_genres = predict(data['Summary'])

    out = pd.DataFrame({
        'Title': data['Title'],
        # 'Summary': data['Summary'],
        'Genres': predicted_genres
    })
    out.to_csv('../out.csv', encoding='utf-8')


classify_file('../data/data-test.csv')
