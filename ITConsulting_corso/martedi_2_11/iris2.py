import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Carica il dataset Iris
data = load_iris()
X = data.data
y = data.target


# 2. Standardizza le caratteristiche utilizzando StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 3. Suddividi i dati in training e test set (70% training, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)


# 4. Applica l'algoritmo DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)


# 5. Valuta la performance del modello utilizzando il classification_report
y_pred = clf.predict(X_test)
report = classification_report(y_test, y_pred, target_names=data.target_names)
print("Classification Report:\n", report)


# 6. Visualizza la matrice di confusione
cm = confusion_matrix(y_test, y_pred)


# Visualizzazione della matrice di confusione
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',

            xticklabels=data.target_names,

            yticklabels=data.target_names)

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()