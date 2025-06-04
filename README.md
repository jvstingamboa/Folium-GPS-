# GPS Data Automation & Anomaly Detection

## Overview

This project demonstrates automated collection, visualization, and basic anomaly detection of GPS (GNSS) data using Python. It simulates GPS data points, visualizes them on an interactive map, and uses a simple machine learning model to detect outlier locations. The project showcases Python scripting, geospatial data handling, automation/testing, and basic ML—all in under 30 minutes.

---

## Features

- **Automated GPS Data Collection:** Simulates a series of GPS points based on your current location.
- **Visualization:** Plots the GPS path and points on an interactive map using Folium.
- **Anomaly Detection:** Uses Isolation Forest (scikit-learn) to identify outlier GPS points.
- **Basic Automation/Test:** Includes a simple test to verify data collection.

---

## Requirements

- Python 3.7+
- [geocoder](https://pypi.org/project/geocoder/)
- [folium](https://pypi.org/project/folium/)
- [scikit-learn](https://scikit-learn.org/stable/)

Install dependencies with:

pip install geocoder folium scikit-learn


---

## Usage

1. **Clone or Download the Repository**

2. **Run the Script**
    ```
    python gps_automation.py
    ```

3. **Output**
    - An interactive map (`gps_path.html`) will be generated in your project folder. Open it in your browser to view the GPS path and points.
    - Console output will display any detected outlier GPS points.
    - A basic test will confirm correct data collection.

---

## How It Works

- **Data Collection:**  
  Uses your IP-based location as a starting point. Simulates movement by adding random jitter to latitude and longitude, and injects an artificial outlier.

- **Visualization:**  
  Plots all collected points and the movement path on a Folium map.

- **Anomaly Detection:**  
  Applies Isolation Forest to flag GPS points that deviate significantly from the others.

- **Testing:**  
  Simple assert-based test checks the number of collected points.

---

## Example Output

- **Map:**  
  *(Open `gps_path.html` in your browser to view the path and markers.)*

- **Console:**
    ```
    Map saved as gps_path.html
    Outlier GPS points:
    (37.4219999, -122.0840575)
    Test passed: Correct number of GPS points collected.
    ```

---

## Why This Project?

This project is designed to demonstrate practical skills relevant to QA and engineering roles involving location technologies:

- Python scripting & automation
- GNSS/GPS data handling
- Visualization and reporting
- Basic machine learning for anomaly detection
- Automated testing

---

## License

MIT License


