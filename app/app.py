from flask import Flask, request, Response

from model import load_model, create_csv

app = Flask(__name__)

model = load_model()


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # data has to be a list of dict with a required field "dialogId"
    data = request.get_json(silent=True)

    # y_pred has to be a (n, 2) list (1st column corresponds to Alice's scores)
    y_pred = app.model.predict(data)
    csv = create_csv(data, y_pred)

    return Response(
        csv,
        mimetype='text/csv',
        headers={'Content-disposition': 'attachment; filename=predictions.csv'}
    )


if __name__ == '__main__':
    app.model = load_model()
    app.run(host='0.0.0.0')
