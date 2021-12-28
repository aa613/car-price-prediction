# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d9U41cEAeUyGnkNBWIgd01S6OGUdjgDG

Importing the dependencies
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics

"""Data Uploading"""

car_dataset=pd.read_csv("/content/car data.csv")
print(car_dataset)

car_dataset.head()

car_dataset.shape

car_dataset.info()

car_dataset.isnull().sum()

print(car_dataset.Fuel_Type.value_counts())

print(car_dataset.Seller_Type.value_counts())

print(car_dataset.Transmission.value_counts())

"""Data-pre-processing"""

car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)

car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

car_dataset.head()

"""Splitting the data into Training data and Target"""

X= car_dataset.drop(['Car_Name','Selling_Price'],axis=1)
Y=car_dataset['Selling_Price']

print(X)

"""Target Data"""

print(Y)

"""Splitting Training and Test data"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,random_state=2)

"""Model Training

1.Linear Regression
"""

# loading the linear regression model
lin_reg_model=LinearRegression()

lin_reg_model.fit(X_train,Y_train)

"""Model Evaluation"""

# prediction of training data
training_data_prediction=lin_reg_model.predict(X_train)

# R squared Error
error_scored=metrics.r2_score(Y_train,training_data_prediction)
print('R squared Error:',error_scored)

"""Visualize the actual prices and Predicted prices"""

plt.scatter(Y_train,training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

# prediction of training data
test_data_prediction=lin_reg_model.predict(X_test)

# R squared Error
error_scored=metrics.r2_score(Y_test,test_data_prediction)
print('R squared Error:',error_scored)

plt.scatter(Y_test,test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

"""Above Model Is Based On Linear Regression Model and now we will feed data in Lasso Model for best fitting of Data

Lasso Regression
"""



# loading the linear regression model
lass_reg_model=Lasso()

lass_reg_model.fit(X_train,Y_train)

"""Model Evaluation"""

# prediction of training data
training_data_prediction=lass_reg_model.predict(X_train)

# R squared Error
error_scored=metrics.r2_score(Y_train,training_data_prediction)
print('R squared Error:',error_scored)

"""Visualize the actual prices and predicted prices"""

plt.scatter(Y_train,training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

# prediction of training data
test_data_prediction=lass_reg_model.predict(X_test)

# R squared Error
error_scored=metrics.r2_score(Y_test,test_data_prediction)
print('R squared Error:',error_scored)

plt.scatter(Y_test,test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

"""So we can Use multiple models to visualise our data prediction"""