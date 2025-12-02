# Importazione delle librerie necessarie
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


# Caricamento del dataset

data = load_iris()

X = data.data  # le caratteristiche

y = data.target  # le etichette


# Divisione dei dati in set di addestramento e di test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Creazione del modello di classificazione

model = RandomForestClassifier(n_estimators=100, random_state=42)


# Addestramento del modello

model.fit(X_train, y_train)


# Predizione delle etichette per il set di test

predictions = model.predict(X_test)


# Calcolo dell'accuratezza del modello

accuracy = accuracy_score(y_test, predictions)

print(f'Accuracy: {accuracy:.2f}')

from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)  # 5-fold CV
print(scores)
print("Media CV:", scores.mean())
