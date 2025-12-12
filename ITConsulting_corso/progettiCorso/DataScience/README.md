# Analisi dei Meteoriti sulla Terra 🚀

Benvenuti nel progetto di analisi dei **meteoriti ritrovati sulla Terra**, basato sul dataset ufficiale della NASA (*Meteorite Landings*).  
Questo progetto ha l’obiettivo di esplorare, pulire, analizzare e modellare i dati per comprendere meglio le caratteristiche dei meteoriti e i fattori che ne influenzano il tipo di ritrovamento (caduto naturalmente o ritrovato).

---

## 🔍 Panoramica del dataset

Il dataset originale contiene oltre **10.000 record** di meteoriti, con informazioni come:

- Massa (`mass (g)`)  
- Coordinate geografiche (`reclat`, `reclong`)  
- Anno di ritrovamento o caduta (`year`)  
- Tipo di ritrovamento (`fall`: Fell/Found)  
- Classe del meteorite (`recclass`)  

Il dataset contiene valori mancanti, duplicati e outlier, quindi una fase di **pulizia e preprocessing** è stata essenziale per ottenere un dataset affidabile.

---

## 🧹 Pulizia dei dati

Durante la fase di preprocessing sono stati effettuati i seguenti passaggi:

1. **Rimozione dei valori mancanti critici**, soprattutto per `mass`, coordinate e `fall`.  
2. **Gestione dei duplicati**, considerando `name` e `mass (g)` come identificatori logici.  
3. **Trattamento degli outlier**, usando il metodo IQR per la maggior parte delle colonne numeriche.  
4. **Standardizzazione delle stringhe**, rimuovendo spazi, valori nulli o incongruenti.  
5. **Ottimizzazione dei tipi di dato**, convertendo le colonne numeriche in tipi più leggeri (`uint8/16/32`, `float32`) e le categorie in `category` per risparmiare memoria.  
6. **Conversione della colonna `year`** in anno numerico pulito (`discovery_year`).  

Il dataset pulito è stato salvato come **`meteorite_clean.csv`** e rappresenta la base per tutte le analisi successive.

---

## ⚙️ Feature Engineering

Per rendere i dati più utili al Machine Learning e all’analisi esplorativa, sono state create nuove colonne:

### Temporali
- `year_normalized`: anno normalizzato tra 0 e 1  
- `decade`: decade di appartenenza del meteorite  
- `age`: età del meteorite (2025 - anno)  
- `is_modern` / `is_recent`: indicatori se il meteorite è moderno o recente  

### Geografiche
- `abs_lat` / `abs_long`: valore assoluto delle coordinate  
- `hemisphere_north` / `hemisphere_east`: indicatori di emisfero  
- `dist_from_equator` / `dist_from_prime_meridian`: distanza dall’equatore o dal meridiano  
- `lat_rad` / `long_rad`: latitudine e longitudine in radianti  
- `quadrant`: quadrante geografico (NE, NW, SE, SW)  

### Massa e interazioni
- `log_mass` / `mass_sqrt`: trasformazioni della massa  
- `mass_category`: classificazione in `very_small`, `small`, `medium`, `large`  
- `is_large` / `is_tiny`: indicatori basati sui quartili  
- Interazioni tra massa, età e latitudine (`mass_x_age`, `mass_x_lat`, `lat_x_long`, `age_x_lat`)  

### Classe e densità
- `class_group`: prima lettera della classe (`recclass`)  
- `recclass_encoded`: encoding numerico della classe  
- `grid_density`: numero di meteoriti in celle geografiche 10x10  

---

## 📊 Analisi esplorativa dei dati (EDA)

L’analisi ha evidenziato diversi pattern interessanti:

1. **Distribuzione della massa**: molto skewata, quindi visualizzata tramite log-transform.  
2. **Tipo di ritrovamento (`fall`)**: caduti (`Fell`) vs ritrovati (`Found`).  
3. **Top 10 classi di meteoriti**: evidenziate per comprendere le classi più frequenti.  
4. **Distribuzione geografica**: scatter plot dei meteoriti nel mondo.  
5. **Violin plot della massa per classe e tipo di ritrovamento**: permette di vedere differenze tra caduti e ritrovati.  

Tutti i grafici principali sono stati salvati come file PNG per documentare l’analisi.

---

## ⚡ Clustering K-Means

Per esplorare pattern non supervisionati:

- Features utilizzate: log_mass, coordinate, anno normalizzato, età, densità, interazioni.  
- Numero di cluster ottimale determinato con **Elbow Method** e **Silhouette Score**.  
- Visualizzazione dei cluster in **2D usando PCA**, per osservare le principali differenze tra gruppi di meteoriti.

---

## 🤖 Machine Learning Supervisionato

Obiettivo: predire se un meteorite è **caduto** o **ritrovato** (`fall_binary`).

- **Modelli testati**: Logistic Regression, Random Forest, Gradient Boosting, XGBoost, LightGBM  
- **Metriche di valutazione**: accuracy, classification report, confusion matrix  
- Il miglior modello è stato selezionato in base all’**accuracy su test set**.  

L’analisi mostra che la massa, la posizione geografica e l’età del meteorite sono le feature più influenti nella predizione del tipo di ritrovamento.

---

## 📂 Output del progetto

- Dataset pulito: `meteorite_clean.csv`  
- Grafici principali (EDA e clustering): `eda_*.png`, `meteorite_*.png`  
- Modelli ML addestrati salvabili con **joblib**  

```python
import joblib
joblib.dump(best_model, 'best_model.pkl')
