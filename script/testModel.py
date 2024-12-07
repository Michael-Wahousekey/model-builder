import joblib
import os
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
import sys
import shutil

def load_test_data():
    # Load California Housing dataset
    housing = fetch_california_housing()
    # Limit to 50 vals since you have a toaster machine
    X = housing.data[:50]
    y = housing.target[:50]
    return X, y

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2

def main():
    # Load test data
    X_test, y_test = load_test_data()

    # Get list of all model files in /models
    model_dir = '/models'
    model_files = [f for f in os.listdir(model_dir) if f.endswith('.pkl')]
    
    best_mse = float('inf')
    best_model = None
    best_model_filename = None

    # Evaluate all models in the /models directory
    for model_filename in model_files:
        model_path = os.path.join(model_dir, model_filename)
        print(f"Evaluating model: {model_filename}")
        
        # Load the model
        model = joblib.load(model_path)
        
        # Evaluate the model
        mse, r2 = evaluate_model(model, X_test, y_test)
        print(f"Model: {model_filename} - Mean Squared Error (MSE): {mse}")
        print(f"Model: {model_filename} - R-squared (R²): {r2}")
        
        # Check if this model is the best so far
        if mse < best_mse:
            best_mse = mse
            best_model = model
            best_model_filename = model_filename

    # If a best model is found, copy it to the root directory
    if best_model:
        print(f"The best model is: {best_model_filename} with MSE: {best_mse}")
        best_model_path = os.path.join(model_dir, best_model_filename)
        
        # Copy the best model to the root directory
        shutil.copy(best_model_path, '/best_model.pkl')
        print(f"Best model saved to /best_model.pkl")
        
        # Optionally, you can also return the best model as needed:
        # joblib.dump(best_model, '/best_model.pkl')
        
        sys.exit(0)
    else:
        print("No models found in /models.")
        sys.exit(1)

if __name__ == "__main__":
    main()