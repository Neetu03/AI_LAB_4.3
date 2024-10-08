# -*- coding: utf-8 -*-
"""lab_assignment_4.3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZAPSzrMAG3-VEIO3tN26BQ5otEXwVke7
"""

import zipfile
zip_file_path = '/content/thyroid+disease.zip'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('/content/')

import pandas as pd
import matplotlib.pyplot as plt

columns = ["Class", "a", "b" ,"c" ,"d" ,"e"]

import csv
with open('new-thyroid.data', 'r') as infile, open('data.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(columns)

    for line in infile:
        data = line.strip().split(',')
        writer.writerow(data)

df = pd.read_csv('data.csv')
df

from sklearn.model_selection import train_test_split
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

