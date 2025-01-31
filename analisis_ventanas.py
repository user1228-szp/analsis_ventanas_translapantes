import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Variables globales
WINDOW_TIME = 1.0  # Duración de la ventana en segundos
BASE_PATH = "/home/manuel/Descargas"  # Ruta base para los archivos
SIGNAL_FILE_1 = os.path.join(BASE_PATH, "movimiento0_001.csv")
SIGNAL_FILE_2 = os.path.join(BASE_PATH, "signal2.csv")
SAMPLING_RATE = 1000  # Frecuencia de muestreo en Hz

def load_signal(file):
    """Carga una señal desde un archivo CSV y genera una columna de tiempo si es necesario."""
    data = pd.read_csv(file, header=None, names=['value'])  # Leer archivo sin encabezados
    data['time'] = np.arange(len(data)) / SAMPLING_RATE  # Generar columna de tiempo
    return data

def apply_overlapping_windows(data, window_time, sampling_rate):
    """Aplica ventanas traslapantes a la señal."""
    step_size = int(window_time * sampling_rate / 2)  # 50% de traslape
    window_size = int(window_time * sampling_rate)
    windows = []
    times = []
    for start in range(0, len(data) - window_size + 1, step_size):
        windows.append(data[start:start + window_size]['value'].values)
        times.append(data['time'].iloc[start])
    return windows, times

def analyze_window(window):
    """Realiza un análisis básico de una ventana."""
    mean = np.mean(window)
    std = np.std(window)
    max_value = np.max(window)
    min_value = np.min(window)
    return {
        "mean": mean,
        "std": std,
        "max": max_value,
        "min": min_value
    }

def main():
    print(f"Primeros tiempos de times_signal1: {times_signal1[:5]}")

    # Cargar señales
    signal1 = load_signal(SIGNAL_FILE_1)
    signal2 = load_signal(SIGNAL_FILE_2)

    # Aplicar ventanas traslapantes
    windows_signal1, times_signal1 = apply_overlapping_windows(signal1, WINDOW_TIME, SAMPLING_RATE)
    windows_signal2, times_signal2 = apply_overlapping_windows(signal2, WINDOW_TIME, SAMPLING_RATE)

    # Analizar ventanas
    analysis_signal1 = [analyze_window(window) for window in windows_signal1]
    analysis_signal2 = [analyze_window(window) for window in windows_signal2]

    # Mostrar resultados con tiempo
    print("Análisis de la señal 1:")
    for i, (analysis, time) in enumerate(zip(analysis_signal1, times_signal1)):
        print(f"Ventana {i + 1} (Tiempo: {time:.2f}s): {analysis}")

    print("\nAnálisis de la señal 2:")
    for i, (analysis, time) in enumerate(zip(analysis_signal2, times_signal2)):
        print(f"Ventana {i + 1} (Tiempo: {time:.2f}s): {analysis}")

    # Visualización de ventanas
    plt.figure(figsize=(10, 6))
    for i, (window, time) in enumerate(zip(windows_signal1, times_signal1)):
        plt.plot(np.linspace(time, time + WINDOW_TIME, len(window)), window, label=f'Ventana {i+1}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Ventanas de la Señal 1')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

