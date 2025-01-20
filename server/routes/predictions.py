from flask import Blueprint, jsonify

predictions_bp = Blueprint('predictions', __name__)

@predictions_bp.route('/', methods=['GET'])
def get_predictions():
    # Placeholder data for stock predictions
    predictions = [
        {'stock': 'AAPL', 'predicted_price': 150.25, 'signal': 'Buy'},
        {'stock': 'MSFT', 'predicted_price': 305.10, 'signal': 'Hold'},
        {'stock': 'GOOGL', 'predicted_price': 2800.75, 'signal': 'Sell'}
    ]
    return jsonify(predictions)
