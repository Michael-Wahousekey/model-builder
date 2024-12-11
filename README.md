### Randomize Hyper Parameters     
```yaml
param_grid = {
    'n_estimators': [random.randint(1, 10), random.randint(25, 50), random.randint(75, 150)],
    'max_depth': [random.randint(1, 5), random.randint(10, 15), random.randint(20, 25)],
    'min_samples_split': [random.randint(1, 2), random.randint(5, 7), random.randint(10, 12)],
    'min_samples_leaf': [1 , random.randint(2, 3), 4]
}
```

### Test Model
1. Aggregate all models from training
2. Get latest model from minio models bucket
3. Test all model which has better MSE and R^2
4. Upload to minio
    - This means that the best model is uploaded
    - If the current model from minio is still the best then it will just upload that model
    - replacing the same model (essentially the same model file) (Can add script to ignore upload...)


### Prediction Values
```yaml
MedInc: Median income in block group.
HouseAge: Median house age in block group.
AveRooms: Average number of rooms per household.
AveOccup: Average number of occupants per household.
Latitude: Latitude of the block group.
Longitude: Longitude of the block group.
Population: Total population in the block group.
MedHouseVal: Median house value for households within the block group.
```

#### Results:
```yaml
{
    "prediction": 4.232466666666668,
    "drift_detected": false
}
```
- Roughly Estimated: 4.23247 * $100,000 = $423,247