import numpy as np
import matplotlib.pyplot as plt
from utils import plot_temperatures, save_data_to_file, load_data_from_file


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

    # Plot the generated dataset
    plt.figure(figsize=(10, 6))
    plt.plot(engine_temps, label='Engine Temperature')
    plt.axhline(y=195, color='r', linestyle='--', label='Lower Limit (195°F)')
    plt.axhline(y=220, color='r', linestyle='--', label='Upper Limit (220°F)')
    plt.title('Simulated Engine Temperature Readings with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°F)')
    plt.legend()
    plt.show()

    return engine_temps, normal_temps

def gaussian_distribution(x, mean, std):
    """Returns the probability of x under a Gaussian distribution."""
    exponent = np.exp(-0.5 * ((x - mean) / std) ** 2)
    return (1 / (np.sqrt(2 * np.pi) * std)) * exponent

# Step 2: Anomaly detection
def detect_anomalies(engine_temps, normal_temps):
    mean = np.mean(normal_temps)
    std = np.std(normal_temps)

    # Define a threshold for anomaly detection (2.5 standard deviations from the mean)
    threshold = 2.5
    anomalies_detected = []

    for temp in engine_temps:
        z_score = (temp - mean) / std  # Calculate the z-score
        if abs(z_score) > threshold:
            anomalies_detected.append(temp)

    print(f"Detected {len(anomalies_detected)} anomalies: {anomalies_detected}")

if __name__ == "__main__":
    # Generate data
    engine_temps, normal_temps = generate_data()
    
    # Detect anomalies
    detect_anomalies(engine_temps, normal_temps)
