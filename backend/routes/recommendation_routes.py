from flask import Blueprint, jsonify, request
import joblib
from config import Config

recommendation_routes = Blueprint('recommendation_routes', __name__)

# Load the Recommender model
model = joblib.load(Config.RECOMMENDER_MODEL_PATH)

# Optionally load the dataset if needed for any purpose
# recommendation_data = pd.read_csv(Config.AMAZON_DATASET_PATH)

@recommendation_routes.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    # Use the model to generate recommendations when ready
    recommendations = model.predict([data['features']])  # Replace 'features' with the actual input format

    return jsonify({"recommendations": recommendations})
