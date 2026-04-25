# 🎓 Student Performance Prediction System

> A machine learning project that predicts final student grades and identifies at-risk students early using academic, behavioral, and demographic data.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Overview

Educational institutions need better ways to:

* Predict student final performance accurately
* Detect struggling students before exams
* Improve intervention strategies using data

This project solves both using a **dual-model machine learning system**.

---

## 🧠 Dual Model Architecture

| Model      | Purpose                | Features Used       |
| ---------- | ---------------------- | ------------------- |
| Model A | Final Grade Prediction | Includes `G1`, `G2` |
| Model B | Early Warning System   | Excludes `G1`, `G2` |

---

## 📂 Dataset

**Source:** UCI Student Performance Dataset

**File Used:** `student-mat.csv`

**Target Variable:** `G3` (Final Grade: 0–20)

---

## ⚙️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook

---

## 🔄 Workflow

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

---

## 🔧 Data Preprocessing

✔ Removed duplicates <br>
✔ Checked missing values <br>
✔ Encoded binary categorical columns <br>
✔ One-hot encoded multi-class variables <br>
✔ Train/Test split

---

## 🤖 Algorithms Compared

* Linear Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

---

## 📊 Evaluation Metrics

* MAE → Mean Absolute Error
* RMSE → Root Mean Squared Error
* R² Score → Goodness of fit

---

## 🏆 Final Selected Models

### 🎯 Model A — Final Grade Predictor

* Uses `G1`, `G2`
* High accuracy
* Best for final score prediction

### 🚨 Model B — Early Warning System

* Excludes `G1`, `G2`
* Predicts performance before exams
* Helps identify at-risk students

---

## 📈 Key Findings

Top factors influencing performance:

* Previous failures
* Study time
* Absences
* Parental education
* Family support
* Motivation for higher education

---

## 📊 Visual Outputs

* Actual vs Predicted plots
* Feature Importance charts
* Model Comparison charts

---

## 💾 Saved Models

```bash
models/
├── model_A_final_grade.pkl
├── model_B_early_warning.pkl
```

---

## 🚀 Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ArunodiAAL/Student-Performance-Prediction-System.git
cd Student-Performance-Prediction-System
```

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch Notebook

```bash
jupyter notebook
```

---

## 📌 Real-World Impact

This system can help schools:

* Detect struggling students early
* Improve intervention planning
* Reduce dropout/failure rates
* Support data-driven decisions

---

# Contact

For questions or feedback:

Email: arunodi520@gmail.com
---
