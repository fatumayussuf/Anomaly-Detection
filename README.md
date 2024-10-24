Efficient Data Stream Anomaly Detection


Overview
This project focuses on detecting anomalies in car engine temperatures using a Gaussian distribution-based anomaly detection system. The goal is to identify engine temperatures that deviate from the expected operating range, which is 195°F to 220°F for a typical petrol engine. The system uses real-time data and flags abnormal temperatures for further inspection.

 Objectives
    Implement Gaussian distribution-based anomaly detection.
    Simulate real-time data streaming using Python generators.
    Handle concept drift using a sliding window mechanism.
    Visualize data and detected anomalies in real-time.

Project Structure
    /car-engine-anomaly-detection
    │
    ├── /src
    │   ├── anomaly_detection.py    # Main script for anomaly detection
    │   ├── data.py                 # Script to generate and visualize synthetic engine temperature data
    │   └── utils.py                # Utility functions (plotting, data saving/loading)
    │
    ├──requirements.md
    └── README.md                   # Project overview and instructions


Features

    1.Data Generation: Simulates normal car engine temperatures with some anomalies.
    2.Anomaly Detection: Detects anomalies in the temperature readings based on a statistical threshold (Gaussian distribution).
    3.Data Visualization: Displays a graph showing engine temperatures with anomalies highlighted.
    4.Data Persistence: Ability to save and load generated datasets for reproducibility.

Requirements
    To install the required dependencies, run the following command:

        pip install -r requirements.txt

Dependencies:

    numpy: For numerical computations.
    matplotlib: For plotting the temperature data and anomalies.

Usage

    Clone the Repository
    git clone https://github.com/fatumayussuf/car-engine-anomaly-detection.git
    cd car-engine-anomaly-detection

 Running the Code
    To generate synthetic data and detect anomalies, run the main script:

    python src/anomaly_detection.py

 Visualization
    A plot of the engine temperature readings and detected anomalies will be displayed using matplotlib. 

Example Output
    The system will print the number of detected anomalies and display the following plot:

    Temperature Readings: A graph showing the simulated engine temperatures over time.
    Detected Anomalies: Anomalous points are highlighted in red.

Contributing
    Contributions are welcome! Please submit a pull request or open an issue if you have any suggestions or improvements.

License
    This project is licensed under the MIT License. See the LICENSE file for more details.