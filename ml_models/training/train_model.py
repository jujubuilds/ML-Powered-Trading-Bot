import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

def train_stock_model(data_file, model_file):
    """Train a stock price prediction model."""
    df = pd.read_csv(data_file)
    X = df[['Open', 'High', 'Low', 'Volume']]
    y = df['Close']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model
    with open(model_file, 'wb') as f:
        pickle.dump(model, f)
    print('Model trained and saved to', model_file)

if __name__ == '__main__':
    train_stock_model('../../data/historical_stock_data.csv', '../lstm_model.pkl')
