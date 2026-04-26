# 🎓 Student Performance Prediction System


![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![R2 Score](https://img.shields.io/badge/R2-0.81-brightgreen?style=for-the-badge)



> 🚀 A machine learning web application that predicts final student grades and identifies at-risk students early using academic, behavioral, and demographic data.

---

## 📌 Overview

Educational institutions need smarter ways to:

- Predict student final performance accurately  
- Detect struggling students before exams  
- Improve intervention strategies using data  

This project addresses these challenges using a **dual-model machine learning system** deployed as an interactive web application. 

## 🧠 Dual Model Architecture

| Model      | Purpose                | Features Used       |
|------------|------------------------|--------------------|
| 🎯 Model A | Final Grade Prediction | Includes `G1`, `G2` |
| 🚨 Model B | Early Warning System   | Excludes `G1`, `G2` |

## 🖥️ Web Application (Streamlit)

The system is built using Streamlit and includes:

- Interactive sliders & inputs  
- Real-time predictions  
- Risk classification system  
- Feature importance visualization  

## 📂 Dataset

- **Source:** UCI Student Performance Dataset  
- **File:** `student-mat.csv`  
- **Target Variable:** `G3` (Final Grade: 0–20)

## ⚙️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Joblib  
- Streamlit  

## 🔄 Project Workflow


```text
Data Collection
   ↓
Cleaning & Encoding
   ↓
EDA & Basic Visualization
   ↓
Model Training
   ↓
Evaluation
   ↓
Insights
```

## 🔧 Data Preprocessing

✔ Removed duplicates  
✔ Handled missing values  
✔ Encoded categorical variables  
✔ Feature selection  
✔ Train/Test split  

## 🤖 Algorithms Compared

- Linear Regression  
- Lasso Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Gradient Boosting Regressor  

## 📊 Evaluation Metrics

- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  

## 🏆 Final Models

### 🎯 Model A — Final Grade Predictor
- Uses `G1`, `G2`  
- High accuracy (~0.81 R²)  
- Best for final prediction  

### 🚨 Model B — Early Warning System
- Excludes exam scores  
- Predicts risk early  
- Helps proactive intervention  

## 📈 Key Insights

- Previous failures strongly reduce performance  
- Study time improves grades  
- Absences negatively impact results  
- Parental education plays a role  
- Internet access & support matter  

## 📊 Visualizations

- Feature Importance Chart  
- Model Comparison  
- Prediction Analysis  

## 💾 Saved Models
```bash
model/
├── model_A_final_grade.pkl
├── model_B_final_grade.pkl
├── model_A_columns.pkl
├── model_B_columns.pkl
```
## 🚀 Run Locally

1. Clone Repository  
```bash
git clone https://github.com/ArunodiAAL/Student-Performance-Prediction-System.git  
cd Student-Performance-Prediction-System  
```
2. Install Requirements  
```bash
pip install -r requirements.txt  
```

3. Run App  
```bash
streamlit run app.py 
``` 

## 🌍 Deployment

Deploy using Streamlit Cloud  

## 📧 Contact

Email: arunodi520@gmail.com
