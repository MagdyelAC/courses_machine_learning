# Define the model
my_model_3 = XGBRegressor(n_estimators=1)

# Fit the model
my_model_3.fit(X_train, y_train)
 # Your code here

# Get predictions
predictions_3 = ____

# Calculate MAE
mae_3 = ____

# Uncomment to print MAE
# print("Mean Absolute Error:" , mae_3)

# Check your answer
step_3.check()