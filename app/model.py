import StringIO

import pandas as pd


class Model(object):
    def predict(self, data):
        return [[0, 1]] * len(data)


def load_model():
    return Model()


def create_csv(data, y_pred):
    rows = []

    for data_i, (alice_score, bob_score) in zip(data, y_pred):
        rows.append({
            'dialogId': data_i['dialogId'],
            'Alice': alice_score,
            'Bob': bob_score
        })

    df = pd.DataFrame(rows, columns=['dialogId', 'Alice', 'Bob'])

    buffer = StringIO.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    csv = buffer.getvalue()
    buffer.close()
    return csv
