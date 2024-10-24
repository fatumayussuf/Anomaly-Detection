import numpy as np
import matplotlib.pyplot as plt

def plot_temperatures(engine_temps, anomalies_detected):
    """Plots engine temperature readings and highlights detected anomalies."""
    plt.figure(figsize=(10, 6))
    plt.plot(engine_temps, label='Engine Temperature')
    plt.axhline(y=195, color='r', linestyle='--', label='Lower Limit (195°F)')
    plt.axhline(y=220, color='r', linestyle='--', label='Upper Limit (220°F)')
    plt.scatter(np.arange(len(engine_temps)), engine_temps,
                c=['r' if (temp in anomalies_detected) else 'b' for temp in engine_temps],
                label='Anomalies', zorder=5)
    plt.title('Engine Temperature Readings with Anomalies Detected')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°F)')
    plt.legend()
    plt.show()

def save_data_to_file(data, filename):
    """Saves the generated temperature data to a specified file."""
    np.save(filename, data)
    print(f"Data saved to {filename}")

def load_data_from_file(filename):
    """Loads temperature data from a specified file."""
    try:
        data = np.load(filename)
        print(f"Data loaded from {filename}")
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
