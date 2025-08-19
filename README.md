# Student Performance Predictor

[![Project Status: Active](https://img.shields.io/badge/status-active-success.svg)](https://github.com/your-username/your-repo)
[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

This project implements an end-to-end machine learning pipeline to predict student performance based on various factors such as gender, ethnicity, parental education, lunch type, test preparation course, writing score, and reading score. The project includes data ingestion, data transformation, model training, and a Flask-based web application for making predictions.

---

## 🚀 Demonstration

This short GIF showcases the web application's interface where users can input student data and receive a predicted academic performance score in real-time.

*(**Pro Tip:** Record your screen while using the app, convert it to a GIF, and place it in a `gifs` folder in your repo!)*

![Project Demo GIF](https://raw.githubusercontent.com/your-username/your-repo/main/path/to/your/demo.gif)

---

## ✨ Features

-   **End-to-End ML Pipeline:** From data ingestion and cleaning to model training and evaluation.
-   **Interactive Web App:** A clean UI built with Flask for easy prediction generation.
-   **In-Depth EDA:** Jupyter notebooks detailing the exploratory data analysis process.
-   **Optimized Model Training:** Utilizes powerful regression models like CatBoost and XGBoost for high accuracy.
-   **Scalable & Modular Code:** A well-organized codebase that is easy to maintain and extend.
-   **Robust Error Handling:** Integrated logging and exception handling for a reliable application.

---

## 🛠️ Tech Stack & Tools

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)

---

## 📂 Project Structure

```text
project-root/
|
+-- app.py                  # Main Flask application entry point
+-- requirements.txt          # Python dependencies and packages
+-- setup.py                  # Installation script for project setup
|
+-- src/                      # Core source code package
|   +-- __init__.py           # Package initialization
|   +-- components/           # Modular ML components
|   |   +-- __init__.py
|   |   +-- data_ingestion.py     # Handles raw data loading
|   |   +-- data_transformation.py# Data cleaning & preprocessing
|   |   L-- model_trainer.py      # Model training and evaluation
|   |
|   +-- pipeline/             # ML workflow pipelines
|   |   +-- __init__.py
|   |   +-- predict_pipeline.py # Prediction workflow
|   |   L-- train_pipeline.py     # Training workflow
|   |
|   +-- exception.py          # Custom exception handling
|   +-- logger.py               # Logging configuration utility
|   L-- utils.py                # Helper functions and utilities
|
+-- notebooks/                # Jupyter notebooks for analysis
|   +-- 1. EDA Student Performance.ipynb # Exploratory Data Analysis
|   L-- 2. Model Training.ipynb        # Model training experiments
|
+-- templates/                # HTML templates for Flask web interface
+-- artifacts/                # Generated files (models, preprocessors, etc.)
L-- README.md                 # Project documentation
```

## ⚙️ Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd student_performance_predictor
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

## ▶️ How TO Run

To run the Flask web application:

1.  **Start the application:**
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5000/` (or the address shown in your terminal).

    You can then input the student's details into the form and click "Predict" to see the estimated performance score.

##  Model Details
The project utilizes various regression models for student performance prediction, including `CatBoost` and `XGBoost`. The models are evaluated using appropriate regression metrics to ensure robust performance. The training process and model selection details can be found in the `2. MODEL TRAINING.ipynb` notebook.

##  📈 Future Enhancements
*   Implement a more sophisticated UI for the web application.
*   Explore additional features that might impact student performance.
*   Integrate with a database for storing predictions and user feedback.
*   Deploy the application to a cloud platform (e.g., AWS, GCP, Azure).

##  📞 Contact
For any questions or suggestions, please feel free to reach out.
