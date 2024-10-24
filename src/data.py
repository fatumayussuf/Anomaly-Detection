import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    """Generates synthetic car engine temperature data with anomalies."""
    np.random.seed(42)

    # Generate normal engine temperature data (in Fahrenheit)
    normal_temps = np.random.normal(loc=205, scale=5, size=1000)  # Mean 205, Std Dev 5

    # Introduce anomalies (extreme temperatures)
    anomalies = np.random.uniform(low=160, high=250, size=20)  # Anomalies far outside the normal range

    # Combine datasets
    engine_temps = np.concatenate([normal_temps, anomalies])
    # Shuffle the dataset to simulate real-world data collection
    np.random.shuffle(engine_temps)

    return engine_temps, normal_temps
