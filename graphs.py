import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

BASE_PATH = "/home/manuel/Descargas"  # Ruta base para los archivos
SIGNAL = os.path.join(BASE_PATH, "movimiento0_002.csv")
SAMPLING_RATE = 1000  # Frecuencia de muestreo en Hz

def load_signal(file):
    data = pd.read_csv(file, header=None).values.flatten()  # Leer archivo y convertirlo en un array plano
    time = np.arange(len(data)) / SAMPLING_RATE  # Generar columna de tiempo
    return time, data

def plot_signal(time, signal):
    """Grafica la señal en función del tiempo."""
    plt.figure(figsize=(10, 6))
    plt.plot(time, signal, label='Señal')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Señal')
    plt.legend()
    plt.grid()
    plt.savefig("signal_plot_2.png")
    plt.show()

def main():
    time, signal = load_signal(SIGNAL)
    plot_signal(time, signal)

if __name__ == "__main__":
    main()
