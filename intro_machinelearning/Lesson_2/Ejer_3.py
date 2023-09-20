from sklearn.tree import DecisionTreeRegressor
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
owa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(X, y)
# Fit the model


# Check your answer
step_3.check()