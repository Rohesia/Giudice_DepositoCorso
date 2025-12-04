import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Impostazione per evitare avvisi di SettingWithCopyWarning
pd.options.mode.chained_assignment = None 

# ==============================================================================
# FUNZIONI DI UTILITÀ
# ==============================================================================

def eval_preds(y_true_log, y_pred_log):
    """
    Valuta RMSE e MAE sulla scala reale (esponenziale del log).
    
    Args:
        y_true_log (array): Valori veri del target in scala logaritmica.
        y_pred_log (array): Valori predetti del target in scala logaritmica.
        
    Returns:
        tuple: (RMSE, MAE) sulla scala reale.
    """
    # Ritorna alla scala reale
    y_true = np.expm1(y_true_log)
    y_pred = np.expm1(y_pred_log)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    return rmse, mae

def group_rare_categories(df, col, threshold=0.01):
    """
    Raggruppa le categorie rare (frequenza < threshold) in 'Other'.
    
    Args:
        df (DataFrame): DataFrame di input.
        col (str): Nome della colonna categorica.
        threshold (float): Soglia di frequenza per considerare una categoria 'rara'.
        
    Returns:
        DataFrame: DataFrame con la colonna modificata.
    """
    freq = df[col].value_counts(normalize=True)
    rare = freq[freq < threshold].index
    df[col] = df[col].replace(rare, 'Other')
    return df

# ==============================================================================
# FASE 1: CARICAMENTO E PULIZIA INIZIALE
# ==============================================================================

def load_and_clean_data(file_path):
    """
    Carica i dati, seleziona le colonne e gestisce i valori mancanti iniziali.
    """
    columns_to_use = ['Suburb', 'Rooms', 'Type', 'Method', 'SellerG', 'Regionname', 
                      'Propertycount', 'Distance', 'CouncilArea', 'Bedroom', 
                      'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'Price']
    
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Errore nel caricamento del file: {e}")
        return pd.DataFrame() 
    
    df = df[columns_to_use].copy()
    
    # Riempimento con 0 (per feature dove NaN può significare assenza)
    cols_fill_0 = ['Car', 'Bathroom', 'Bedroom', 'Distance', 'Propertycount']
    df[cols_fill_0] = df[cols_fill_0].fillna(0)
    
    # Conversione in numerico e riempimento con media
    df['Landsize'] = pd.to_numeric(df['Landsize'], errors='coerce')
    df['BuildingArea'] = pd.to_numeric(df['BuildingArea'], errors='coerce')
    
    # Imputazione con la media
    df['Landsize'].fillna(df['Landsize'].mean(), inplace=True)
    df['BuildingArea'].fillna(df['BuildingArea'].mean(), inplace=True)

    # Rimozione infiniti o residuali NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    
    return df

# ==============================================================================
# FASE 2: GESTIONE OUTLIER
# ==============================================================================

def remove_outliers(df):
    """
    Rimuove gli outlier tramite trimming sui quantili 1% e 99%.
    """
    print("DataFrame prima della rimozione outlier:", len(df))
    
    cols_to_check = ['Price', 'Landsize', 'BuildingArea']
    
    # Applica il trimming per tutte le colonne
    for col in cols_to_check:
        q_low, q_high = df[col].quantile([0.01, 0.99])
        df = df[(df[col] >= q_low) & (df[col] <= q_high)]
        
    print("DataFrame dopo la rimozione outlier:", len(df))
        
    return df

# ==============================================================================
# FASE 3: FEATURE ENGINEERING E ENCODING
# ==============================================================================

def feature_engineer_and_encode(df):
    """
    Crea nuove feature e applica l'One-Hot Encoding.
    """
    
    # Raggruppamento categorie rare
    print("Raggruppamento categorie rare...")
    for col in ['Suburb', 'SellerG', 'Regionname', 'CouncilArea']:
        df = group_rare_categories(df, col) 
        
    # Creazione nuove feature
    print("Creazione nuove feature...")
    df['Rooms_per_Landsize'] = df['Rooms'] / (df['Landsize'] + 1)
    df['TotalRooms'] = df['Rooms'] + df['Bathroom'] + df['Car']
    df['Bath_per_Bed'] = df['Bathroom'] / (df['Bedroom'] + 1)
    df['Rooms_per_Area'] = df['TotalRooms'] / (df['Landsize'] + 1)
    
    # Trasformazione logaritmica (utile per variabili con distribuzione skewata)
    df['Landsize_log'] = np.log1p(df['Landsize'])
    df['BuildingArea_log'] = np.log1p(df['BuildingArea'])
    
    df['Area_per_Room'] = df['Landsize'] / (df['Rooms'] + 1)
    df['BuildingRatio'] = df['BuildingArea'] / (df['Landsize'] + 1)

    # One-Hot Encoding
    print("Applicazione One-Hot Encoding...")
    categorical_cols = ['Suburb', 'Type', 'Method', 'SellerG', 'Regionname', 'CouncilArea']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df

# ==============================================================================
# FASE 4: MODELLAZIONE E PREDIZIONE
# ==============================================================================

def run_models(X_train, X_test, y_train, y_test):
    """
    Addestra e predice con tutti i modelli.
    
    Returns:
        tuple: (models, y_preds, X_test_scaled)
    """
    
    # 1. Scaling per modelli lineari
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    models = {}
    y_preds = {}
    
    # --- Modelli Lineari Regolarizzati ---
    print("\nAddestramento Modelli Lineari...")
    
    # LassoCV (L1)
    lasso_model = LassoCV(alphas=np.logspace(-3,2,20), cv=5, max_iter=10000)
    lasso_model.fit(X_train_scaled, y_train)
    y_preds['Lasso'] = lasso_model.predict(X_test_scaled)
    models['Lasso'] = lasso_model
    
    # RidgeCV (L2)
    ridge_model = RidgeCV(alphas=np.logspace(-2,2,20), cv=5)
    ridge_model.fit(X_train_scaled, y_train)
    y_preds['Ridge'] = ridge_model.predict(X_test_scaled)
    models['Ridge'] = ridge_model
    
    # ElasticNetCV (L1 + L2)
    elastic = ElasticNetCV(l1_ratio=np.linspace(0.1,0.9,9), alphas=np.logspace(-3,2,20), 
                           cv=5, max_iter=10000, random_state=42)
    elastic.fit(X_train_scaled, y_train)
    y_preds['ElasticNet'] = elastic.predict(X_test_scaled)
    models['ElasticNet'] = elastic
    
    # --- Modelli non Lineari (usano dati non scalati) ---
    print("Addestramento Modelli ad Albero (non lineari)...")
    
    # RandomForestRegressor
    rf = RandomForestRegressor(n_estimators=500, max_depth=15, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    y_preds['RandomForest'] = rf.predict(X_test)
    models['RandomForest'] = rf
    
    # XGBRegressor
    xgb = XGBRegressor(n_estimators=500, max_depth=6, learning_rate=0.05, 
                       random_state=42, verbosity=0)
    xgb.fit(X_train, y_train)
    y_preds['XGBoost'] = xgb.predict(X_test)
    models['XGBoost'] = xgb

    return models, y_preds, X_test_scaled, scaler

# ==============================================================================
# FASE 5: VALUTAZIONE E VISUALIZZAZIONE
# ==============================================================================

def evaluate_and_plot(models, y_preds, X_test, y_test, X_test_scaled):
    """
    Calcola le metriche, stampa i risultati e crea il grafico di confronto.
    """
    results = {}
    
    model_names = ['Ridge', 'Lasso', 'ElasticNet', 'RandomForest', 'XGBoost']
    
    for name in model_names:
        y_pred = y_preds[name]
        
        # Determina quale set di dati usare per lo score (scalato o meno)
        X_data = X_test_scaled if name not in ['RandomForest','XGBoost'] else X_test
        r2 = models[name].score(X_data, y_test)
            
        rmse, mae = eval_preds(y_test, y_pred)
        results[name] = {'R2': r2, 'RMSE': rmse, 'MAE': mae}

    # Stampa i risultati
    print("\n" + "="*25)
    print("=== RISULTATI MODELLI ===")
    print("="*25)
    for name, m in results.items():
        print(f"{name}: R² = {m['R2']:.4f}, RMSE = {m['RMSE']:.2f}, MAE = {m['MAE']:.2f}")

    # Plot di confronto
    plt.figure(figsize=(10,6))
    y_test_real = np.expm1(y_test)

    for name in model_names:
        plt.scatter(y_test_real, np.expm1(y_preds[name]), alpha=0.3, label=name)

    plt.plot([0, max(y_test_real)], [0, max(y_test_real)], 'r--', label='Perfetta Predizione')
    plt.xlabel('Prezzo reale')
    plt.ylabel('Prezzo predetto')
    plt.title('Confronto modelli: predetti vs reali')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    
    
# ==============================================================================
# MAIN DRIVER
# ==============================================================================

if __name__ == "__main__":
    
    print("Inizio del pipeline di Machine Learning per i prezzi delle case di Melbourne.")
    
    # --- 1. CONFIGURAZIONE ---
    FILE_PATH = 'Melbourne_housing.csv'
    RANDOM_STATE = 42
    
    # --- 2. CARICAMENTO E PULIZIA INIZIALE ---
    df = load_and_clean_data(FILE_PATH)
    if df.empty:
        print("Impossibile procedere a causa di un errore nel caricamento dati.")
    else:
        # --- 3. GESTIONE OUTLIER ---
        df = remove_outliers(df)
        
        # --- 4. FEATURE ENGINEERING E ENCODING ---
        df = feature_engineer_and_encode(df)
        
        # --- 5. PREPARAZIONE PER MODELLAZIONE ---
        print("\nPreparazione dati per la modellazione...")
        y = np.log1p(df['Price'])  
        X = df.drop('Price', axis=1)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, train_size=0.8, random_state=RANDOM_STATE
        )
        
        # --- 6. MODELLAZIONE ---
        models, y_preds, X_test_scaled, scaler = run_models(X_train, X_test, y_train, y_test)
        
        # --- 7. VALUTAZIONE E VISUALIZZAZIONE ---
        evaluate_and_plot(models, y_preds, X_test, y_test, X_test_scaled)