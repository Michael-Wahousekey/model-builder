import joblib
import os
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
import sys

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

    # Load new model
    new_model = joblib.load('best_rf_model.pkl')

    # Evaluate new model
    new_mse, new_r2 = evaluate_model(new_model, X_test, y_test)
    print(f"New Model - Mean Squared Error (MSE): {new_mse}")
    print(f"New Model - R-squared (R²): {new_r2}")

    # Check if a previous model exists
    previous_model_path = 'previous_rf_model.pkl'
    if os.path.exists(previous_model_path):
        # Load the previous model
        previous_model = joblib.load(previous_model_path)

        # Evaluate previous model
        prev_mse, prev_r2 = evaluate_model(previous_model, X_test, y_test)
        print(f"Previous Model - Mean Squared Error (MSE): {prev_mse}")
        print(f"Previous Model - R-squared (R²): {prev_r2}")

        # Compare the performance
        if new_mse < prev_mse:
            # Success
            print("New model performs better than the previous model.")
            joblib.dump(new_model, previous_model_path)
            sys.exit(0)
        else:
            # Fail
            print("Previous model performs better or is equal to the new model.")
            sys.exit(1)
    else:
        # Success
        print("No previous model found. Using the new model as the baseline.")
        joblib.dump(new_model, previous_model_path) 
        sys.exit(0)

if __name__ == "__main__":
    main()
