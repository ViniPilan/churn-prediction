from flask import Flask, request
from data_prepare import Pipeline
import pandas as pd
import pickle
import os


app = Flask(__name__)

model_file = open('../Models/class_model.pkl', 'rb')
model = pickle.load(model_file)
model_file.close()

@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()
    
    # Collect data
    if test_json:
        if isinstance(test_json, dict): # Unique value
            df = Pipeline.run(pd.DataFrame(test_json, index=[0]))
        else:
            df = Pipeline.run(pd.DataFrame(test_json, columns=test_json[0].keys()))

    # Prediction
    pred = model.predict(df)
    proba = model.predict_proba(df)[:, 1]

    df['Prediction'] = pred
    df['Prediction_prob'] = proba

    return df.to_json(orient='records')


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)

