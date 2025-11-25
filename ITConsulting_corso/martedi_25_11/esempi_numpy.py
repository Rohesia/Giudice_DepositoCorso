# esempi di utilizzo 
# esempio 1

import numpy as np 
# Calcolo matrice quadrata
A = np.array([[1, 2], [3, 4]])

# Calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A: \n", A_inv)

# esempio2 
# ======================================
# ======= NORMA DI UN VETTORE ==========
# ======================================

# creazione di un vettore 
v = np.array([3, 4])

# calcolo della norma del vettore 
norm_v = np.linalg.norm(v)
print("Norma di v: ", norm_v)


# esempio 3 
# ======================================
# ============= SOLVE ==================
# ======================================

# creazione della matrice A e matrice B 
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])

# Risoluzione del sistema di equazione Ax = B
x = np.linalg.solve(A, B)
print("Soluzione x:", x)

# esempio 4 
# ======================================
# =============== DFT ==================
# ======================================

# Creazione di un segnale

t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Calcolo della Trasformata di Fourier
fft_sig = np.fft.fft(sig)

# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)

# esempio 5
# ======================================
# =========== BROADCASTING =============
# ======================================

arr = np.array([1, 2, 3, 4])
scalar = 10

# Broadcasting aggiunge lo scalare ad ogni elemento dell'array 
result = arr + scalar 
print(result)

