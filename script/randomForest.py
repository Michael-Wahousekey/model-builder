# Import necessary libraries
import joblib
import os
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score

# # Get the pod name from the environment variable
pod_name = os.getenv("HOSTNAME")

# # Define the path with the pod name as part of the file name
model_filename = f"models/{pod_name}.pkl"

# Define the path with the pod name as part of the file name
# model_filename = "model-pod_name.pkl"

# Load California Housing dataset
housing = fetch_california_housing()
# Limit to 50 vals since i have a toaster machine
X = housing.data[:50]
y = housing.target[:50]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
rf_model = RandomForestRegressor(random_state=42)

# Define hyperparameter ranges
param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Use GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)

# Fit the model with the hyperparameter search
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_
print(f"Best Parameters: {best_params}")

# Get the best model from the grid search
best_rf_model = grid_search.best_estimator_

# Make predictions on the test set
y_pred = best_rf_model.predict(X_test)

# Evaluate the model using MSE and R²
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")


# Save the best model to a file
joblib.dump(best_rf_model, model_filename)
print("Best model saved")