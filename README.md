# 🎓 Student Performance Prediction System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![R2 Score](https://img.shields.io/badge/R2-0.81-brightgreen?style=for-the-badge)

>  A machine learning web application that predicts final student grades and identifies at-risk students early using academic, behavioral, and demographic data.
---

## 🌐 Live Demo

**Try the App Here:**
 https://arunodiaal-student-performance-prediction-system-app-hhijbu.streamlit.app/


## 📌 Problem Statement

Educational institutions need smarter ways to:

* Predict student final performance accurately
* Detect struggling students before exams
* Improve intervention strategies using data

This project solves these challenges using a **dual-model machine learning system** deployed as an interactive web application.



## 🧠 Key Features

* Dual prediction system (Final + Early Warning)
* Student risk classification (At-risk / Safe)
* Interactive Streamlit UI
* Feature importance visualization
* Real-time predictions
* Pre-trained model integration



## 🧠 Dual Model Architecture

| Model      | Purpose                | Features Used       |
| ---------- | ---------------------- | ------------------- |
| Model A | Final Grade Prediction | Includes `G1`, `G2` |
| Model B | Early Warning System   | Excludes `G1`, `G2` |


## 🖥️ Web Application

Built using **Streamlit**, the application provides:

* User-friendly input interface
* Instant prediction results
* Student risk classification
* Visual analytics dashboard



## 📂 Dataset

* Source: UCI Machine Learning Repository
* File: `student-mat.csv`
* Target Variable: `G3` (Final Grade: 0–20)



## ⚙️ Tech Stack

* Python 
* Pandas & NumPy
* Scikit-learn
* Matplotlib & Seaborn
* Joblib
* Streamlit


## 🔄 Project Workflow

Data Collection → Data Cleaning → EDA → Model Training → Evaluation → Deployment



## 🔧 Data Preprocessing

✔ Removed duplicates  
✔ Handled missing values  
✔ Encoded categorical variables  
✔ Feature selection  
✔ Train/Test split  



## 🤖 Algorithms Compared

* Linear Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor



## 📊 Evaluation Metrics

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score



## 🏆 Model Performance

###  Model A — Final Grade Predictor

* Uses `G1`, `G2`
* High accuracy (~0.81 R²)
* Best for final prediction

###  Model B — Early Warning System

* Excludes exam scores
* Predicts student risk early
* Helps proactive intervention



## 🎯 Business Impact

* Helps teachers identify weak students early
* Enables data-driven academic decisions
* Improves student success rates
* Supports personalized learning strategies



## 📈 Key Insights

* Previous failures strongly reduce performance
* Study time improves grades
* Absences negatively impact results
* Parental education plays a role
* Internet access improves learning support



## 📊 Visualizations

* Feature Importance Chart
* Model Comparison
* Prediction Analysis


## 💾 Saved Models

```
model/
├── model_A_final_grade.pkl
├── model_B_final_grade.pkl
├── model_A_columns.pkl
├── model_B_columns.pkl
```


## 🚀 Run Locally

1. Clone Repository

```
git clone https://github.com/ArunodiAAL/Student-Performance-Prediction-System.git
cd Student-Performance-Prediction-System
```

2. Install Requirements

```
pip install -r requirements.txt
```

3. Run App

```
streamlit run app.py
```


## 🌍 Deployment

Deploy easily using:

* Streamlit Cloud 
* Render


## 📧 Contact

 Email: arunodi520@gmail.com
