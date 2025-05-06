from flask import Blueprint, request, jsonify
from .model import predict_news

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return "Welcome to Fake News Detector API! 🚀"

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    news_text = data.get('text', '')
    prediction = predict_news(news_text)

    return jsonify({"prediction": prediction})
