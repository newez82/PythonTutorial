"""
    machine learning prediction on housing in Medlbourne, Australia
    use the scikit-learn library to create your models.
"""

#############################################################
#                   ML Model - Decision Tree
#############################################################
import pandas as pd

# RandomForest model
from sklearn.ensemble import RandomForestRegressor

# to find the differences between prediction vs actual values
from sklearn.metrics import mean_absolute_error

# split data into training and validation data, for both features and target
from sklearn.model_selection import train_test_split

# Use Desicion Tree training model
from sklearn.tree import DecisionTreeRegressor

MELBOURNE_FILE_PATH = "machine_learning\\kaggle\\data\\melb_data.csv\\melb_data.csv"

melbourne_data = pd.read_csv(MELBOURNE_FILE_PATH)
print(f"load CSV file into DataFrame: \n{melbourne_data.head(10)}")
print(f"show columns within DataFrame:\n{melbourne_data.columns}")

melbourne_data = melbourne_data.dropna(axis=0)

# Prediction Target (y) - select the column we want to predict
y = melbourne_data.Price

# Features - columns used to determine the Prediction Target
melbourne_feature = ["Rooms", "Bathroom", "Landsize", "Lattitude", "Longtitude"]

# X is data tha used to determine the Prediction Target
X = melbourne_data[melbourne_feature]

print(f"Generate descriptive statistics based on the features:\n{X.describe()}")
# print(f"Show the data that determine the Prediction Target:\n{X.head()}")

# Define model by specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Train/Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

print("First in-sample predictions         :", melbourne_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

#############################################################
#                   Model Validation
# We used a single "sample" of houses for both building the
# model and evaluating it. Here's why this is bad.
# we should exclude some data from the model-building process,
# and then use those to test the model's accuracy on data it hasn't
# seen before. This data is called validation data.
#############################################################
# Mean Absolute Error (MAE) - On average, our predictions are off by about X.
predicted_home_prices = melbourne_model.predict(X)
mae = mean_absolute_error(y, predicted_home_prices)
print(f"total number of differences between prediction and actual home price: {mae}")
print("Validation MAE: {:,.0f}".format(mae))

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

print("model validation:")

melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
train_mae = mean_absolute_error(val_y, val_predictions)

print(
    f"total number of differences between prediction and actual home price: {train_mae}"
)

print("First in-sample predictions         :", melbourne_model.predict(val_X.head()))
print("Actual target values for those homes:", val_y.head().tolist())
print("Validation MAE: {:,.0f}".format(train_mae))


#############################################################
#                   Underfitting and Overfitting
# overfitting, where a model matches the training data almost
# perfectly, but does poorly in validation and other new data.
#
# underfitting When a model fails to capture important
# distinctions and patterns in the data, so it performs poorly
# even in training data.
#############################################################
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae


# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(
        "Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" % (max_leaf_nodes, my_mae)
    )

#############################################################
#                   random forest
# The random forest uses many trees, and it makes a prediction
# by averaging the predictions of each component tree.
# It generally has much better predictive accuracy than
# a single decision tree and it works well with default parameters.
#############################################################
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(
    "Random forest Validation MAE: {:,.0f}".format(
        mean_absolute_error(val_y, melb_preds)
    )
)
