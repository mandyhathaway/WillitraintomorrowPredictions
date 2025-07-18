# -*- coding: utf-8 -*-
"""Template for weather prediction model- Beginner.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pr7ysjz36YnkmYcmEW5K9dmuWZPBmUeU
"""

### BUILDING A MACHINE LEARNING MODEL WHICH WILL PREDICT WHETHER OR NOT IT WILL RAIN TOMORROW BY LEARNING FROM PAST DATA ###

### SETUP ###

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, chi2

### STEP 1 ### LOAD THE DATASET ###

df = pd.read_csv('weather.csv')
print('size of data frame =', df.shape)
print(df[0:5])

### STEP 2 ### REMOVE NULL VALUES FROM THE DATA FRAME###

df = df.dropna(how='any')
print('size after removing null values =', df.shape)

### STEP 3 ### HANDLE NON-NUMERIC DATA AND NORMALIZE ###

y = df[['RainTomorrow']]
# Select only numeric columns for X after dropping RISK_MM
X = df.drop(columns=['RISK_MM']).select_dtypes(include=np.number)


scaler = preprocessing.MinMaxScaler()
scaler.fit(X)
X_scaled = pd.DataFrame(scaler.transform(X), index=X.index, columns=X.columns)
print(X_scaled.iloc[4:10])


### STEP 4 ### FEATURE SELECTION ###

selector = SelectKBest(chi2, k=5)
le = preprocessing.LabelEncoder()
y_encoded = le.fit_transform(y.values.ravel())
selector.fit(X_scaled, y_encoded)
X_new = selector.transform(X_scaled)
print(X_scaled.columns[selector.get_support(indices=True)])


### STEP 5 ### PUT IMPORTANT FEATURES IN THE DATA FRAME ###

df = df[['Sunshine', 'Humidity3pm', 'Pressure3pm', 'Cloud9am', 'Cloud3pm']]
df['RainTomorrow'] = y
X = df.drop(columns=['RainTomorrow'])

### STEP 6 ### DATA SPLICING ###



### STEP 7 ### BUILDING THE MODEL USING THE TRAINING DATA SET ###



### STEP 8 ### EVALUATE THE MODEL USING THE TRAINING DATA SET ###


### STEP 9 ### CALCULATE ACCURACY ###


### STEP 10 ###TEST YOUR OWN WEATHER DATA ###

print("\nTry your own weather info to see if it might rain tomorrow!")
sunshine = float(input("Enter Sunshine (hours): "))
humidity3pm = float(input("Enter Humidity at 3pm (%): "))
pressure3pm = float(input("Enter Pressure at 3pm (hPa): "))
cloud9am = float(input("Enter Cloud at 9am (oktas 0–8): "))
cloud3pm = float(input("Enter Cloud at 3pm (oktas 0–8): "))

# Make a single-row DataFrame with the new input
student_input = pd.DataFrame([[sunshine, humidity3pm, pressure3pm, cloud9am, cloud3pm]],
                             columns=['Sunshine', 'Humidity3pm', 'Pressure3pm', 'Cloud9am', 'Cloud3pm'])

# Re-fit scaler only on the features used in the final model
scaler_for_5_features = preprocessing.MinMaxScaler()
scaler_for_5_features.fit(X)  # X is already defined with those 5 columns

# Scale the student input
student_input_scaled = scaler_for_5_features.transform(student_input)

# Ask the model to make a prediction
prediction = clf_logreg.predict(student_input_scaled)

# Show the prediction result
print("\n Prediction: Will it rain tomorrow?")
print("Yes!" if prediction[0] == 1 else "No! ")