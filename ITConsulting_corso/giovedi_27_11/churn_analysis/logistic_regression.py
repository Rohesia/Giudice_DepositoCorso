import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from file import * 

# dati per modellazione 
df['Churn_num'] = df['Churn'].map({'No':0, 'Sì':1})

numerical_cols = ['Età','Durata_Abbonamento','Tariffa_Mensile','Dati_Consumati','Servizio_Clienti_Contatti','Costo_per_GB']
df[numerical_cols] = (df[numerical_cols] - df[numerical_cols].mean()) / df[numerical_cols].std()

# Selezioniamo solo le colonne numeriche per il modello
X = df[['Età','Durata_Abbonamento','Tariffa_Mensile','Dati_Consumati','Servizio_Clienti_Contatti']]
y = df['Churn_num']

# Dividiamo in train e test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Creiamo il modello di regressione logistica
model = LogisticRegression()
model.fit(X_train, y_train)

# Predizioni
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:,1]  # probabilità di churn = 1

# Valutazione
accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_prob)

print(f"Accuracy: {accuracy:.3f}")
print(f"AUC: {auc:.3f}")
