"""
    Linear Regression
        - basic machine learning algorithm.
        - common process used in many applications of statistics
        - used for finding linear relationship between target and one ore more predictors.
          There are 2 types of linear regression:
            1 - Simple
            2 - Multiple
        - line that is best fitting or closest to the points where the X Y coorindates are
          obervations of the 2 variables which are expected to depend linearly on each other.
        - given 2 variable X and Y, the model can predict values of Y given future observation of X.
        - it is used to predict variables in countless situations
            -i.e. outcome of political elections,
          behavior of stock market or the perofrmance of a professional athlete.

        - Cost function helps us to figure out the best possible values for a_0 and a_1
          which would provide the best fit line for the data points.
        - the differences between the predicted value and ground truth measures the error
          difference, sum of all the data points and divide that value by total # of data points,
          that provide average squared error over all the data points. It also knows as mean
          square error.
        - minimize the cost function using gradient descent, is a method of updating a_0 and a_1
          to reduce the cost function (mean square error). It helps us how to change the values.
        - we can either use scikit learn library to import the linear regression mode or implement
          it our own.

    Steps:
        1. Import the data
        2. Clean the data
        3. Split the data into training / test sets
        4. Create a model
        5. Train the model
        6. Make Predictions
        7. Evaluate and Improve

    Libraries
        1. Numpy - provides mulit-dimensional array
        2. Pandas - data analysis - data frame
        3. MatplotLib - 2 dimensional plotting library for creating 
                        graphs and plots
        4. Scikit-Learn - provide algorithms like decision trees, 
                          neural networks and etc.

    installation
        jupyter makes is easy to inspect our data. Use Anaconda platform to install jupyter.
        Anaconda will install jupyter along with other populate data science libraries like
        numpy, panda, etc without install each one manually using pip.

        1. enter jupyter notebook in terminal, it will start jupyter notebook server
        2. open web broswer and type in localhost:8888
"""

# Linear equation y = a_0 + a_1 * x
# x and y are variable that will present in the data set.

# mtaplotlib to visualize the data and result
import matplotlib.pyplot as plt

# panda library to manipulate the dataset
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data/Advertising.csv")

# to see how data look like using head() method
data.head()
