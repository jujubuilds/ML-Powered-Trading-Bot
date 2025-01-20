from flask import Flask, jsonify, request
from routes.predictions import predictions_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(predictions_bp, url_prefix='/api/predictions')

@app.route('/')
def index():
    return jsonify({'message': 'ML Trading Bot API is running'})

if __name__ == '__main__':
    app.run(debug=True)
