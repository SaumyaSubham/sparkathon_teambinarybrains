from flask import Blueprint, jsonify, request
import joblib
import pandas as pd
from config import Config

churn_prediction_routes = Blueprint('churn_prediction_routes', __name__)

# Load the Churn Prediction model
model = joblib.load(Config.CHURN_MODEL_PATH)

# Optionally load the dataset if needed for any purpose
# churn_data = pd.read_csv(Config.TEL_CHURN_DATASET_PATH)

@churn_prediction_routes.route('/predict_churn', methods=['POST'])
def predict_churn():
    data = request.json
    # Assuming the model expects a certain format of input data, e.g., a list of features
    prediction = model.predict([data['features']])  # Replace 'features' with the actual input format

    return jsonify({"churn_prediction": prediction[0]})
