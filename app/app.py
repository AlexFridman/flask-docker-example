from flask import Flask, request, jsonify
from sklearn.dummy import DummyRegressor

app = Flask(__name__)


def load_model():
    X_dummy, y_dummy = [[0], [0]], [1, 1]
    return DummyRegressor().fit(X_dummy, y_dummy)


model = load_model()


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = request.get_json(silent=True)
    y_pred = model.predict([[0], [0]]).tolist()
    return jsonify({'X': data, 'y_pred': y_pred})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
