# ML-Powered Trading Bot

## Overview
A full-stack web application that predicts stock prices using machine learning and automates trading strategies.

### Features
1. **Machine Learning Model**: Predict stock prices with a Random Forest model.
2. **API Integration**: Fetch real-time stock data and provide predictions.
3. **Dashboard**: Visualize stock trends, predictions, and P&L.
4. **Trading Simulator**: Execute simulated trades based on ML predictions.

### Tech Stack
- **Frontend**: React, Chart.js
- **Backend**: Flask, REST API
- **Machine Learning**: scikit-learn, Random Forest

### Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd ml-trading-bot
   ```
2. Install dependencies:
   - For the backend:
     ```bash
     cd server
     pip install -r requirements.txt
     ```
   - For the frontend:
     ```bash
     cd client
     npm install
     ```
3. Train the model:
   ```bash
   cd ml_models/training
   python train_model.py
   ```
4. Start the application:
   - Backend: `python server/app.py`
   - Frontend: `npm start` (from `client` directory).

### Future Enhancements
- Use advanced models like LSTM for time series prediction.
- Add live trading features with brokerage API integration.
- Include crypto trading support.
