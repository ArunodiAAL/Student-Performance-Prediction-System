import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)


st.markdown("""
<style>
.big-title {
    font-size:30px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


def load_file(path):
    if not os.path.exists(path):
        st.error(f"Missing file: {path}")
        st.stop()
    return joblib.load(path)


MODEL_DIR = "model"

model_a = load_file(f"{MODEL_DIR}/model_A_final_grade.pkl")
model_b = load_file(f"{MODEL_DIR}/model_B_final_grade.pkl")

cols_a = load_file(f"{MODEL_DIR}/model_A_columns.pkl")
cols_b = load_file(f"{MODEL_DIR}/model_B_columns.pkl")


st.sidebar.title("🎓 Student AI System")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🎯 Final Grade Predictor",
        "🚨 Early Warning",
        "📊 Insights"
    ]
)



st.markdown('<p class="big-title">🎓 Student Performance Dashboard</p>', unsafe_allow_html=True)

if page == "🏠 Home":

    st.markdown("""Welcome to an **AI-powered academic prediction system**.""")

    col1, col2 = st.columns(2)

    with col1:
        st.info("### 🎯 Final Grade Predictor\nPredicts final exam score using academic data.")

    with col2:
        st.warning("### 🚨 Early Warning System\nDetects at-risk students early.")

    st.success("Use the sidebar to navigate through the system.")

 # MODEL A 

elif page == "🎯 Final Grade Predictor":

    st.header("🎯 Final Grade Predictor")

    col1, col2 = st.columns(2)

    with col1:
        G1 = st.slider("G1 Grade", 0, 20, 10)
        G2 = st.slider("G2 Grade", 0, 20, 10)
        studytime = st.select_slider("Study Time", options=[1,2,3,4])

    with col2:
        failures = st.slider("Past Failures", 0, 4, 0)
        absences = st.slider("Absences", 0, 100, 5)

    famsup = st.selectbox("Family Support", ["No", "Yes"])
    internet = st.selectbox("Internet Access", ["No", "Yes"])
    higher = st.selectbox("Higher Education Goal", ["No", "Yes"])

    # Convert to numeric
    famsup = 1 if famsup == "Yes" else 0
    internet = 1 if internet == "Yes" else 0
    higher = 1 if higher == "Yes" else 0

    if st.button("🚀 Predict Final Grade"):

        input_df = pd.DataFrame(
            np.zeros((1, len(cols_a))),
            columns=cols_a
        )

        values = {
            "G1": G1,
            "G2": G2,
            "studytime": studytime,
            "failures": failures,
            "absences": absences,
            "famsup": famsup,
            "internet": internet,
            "higher": higher
        }

        for col, val in values.items():
            if col in input_df.columns:
                input_df[col] = val

        pred = model_a.predict(input_df)[0]

        st.markdown("### 🎯 Prediction Result")

        st.metric(
            label="Final Grade",
            value=f"{round(pred,2)} / 20"
        )

        if pred >= 15:
            st.success("Excellent Performance 🎉")
        elif pred >= 10:
            st.warning("Average Performance ⚠️")
        else:
            st.error("At Risk ❗")

 # MODEL B

elif page == "🚨 Early Warning":

    st.header("🚨 Early Warning System")

    col1, col2 = st.columns(2)

    with col1:
        failures = st.slider("Past Failures", 0, 4, 0)
        absences = st.slider("Absences", 0, 100, 5)
        studytime = st.select_slider("Study Time", options=[1,2,3,4])

    with col2:
        famsup = st.selectbox("Family Support", ["No", "Yes"])
        internet = st.selectbox("Internet Access", ["No", "Yes"])
        Medu = st.slider("Mother Education", 0, 4, 2)

    # Convert
    famsup = 1 if famsup == "Yes" else 0
    internet = 1 if internet == "Yes" else 0

    if st.button("Check Risk"):

        input_df = pd.DataFrame(
            np.zeros((1, len(cols_b))),
            columns=cols_b
        )

        values = {
            "failures": failures,
            "absences": absences,
            "studytime": studytime,
            "famsup": famsup,
            "internet": internet,
            "Medu": Medu
        }

        for col, val in values.items():
            if col in input_df.columns:
                input_df[col] = val

        pred = model_b.predict(input_df)[0]

        st.markdown("### 🚨 Risk Analysis")

        st.metric("Predicted Grade", round(pred,2))

        if pred >= 15:
            st.success("🟢 Low Risk Student")
        elif pred >= 10:
            st.warning("🟡 Medium Risk Student")
        else:
            st.error("🔴 High Risk Student")

# INSIGHTS

elif page == "📊 Insights":

    st.header("📊 Insights")

    chart = pd.DataFrame({
        "Feature": [
            "G2", "G1", "Failures",
            "Absences", "Study Time",
            "Parental Education"
        ],
        "Importance": [
            0.40, 0.30, 0.10,
            0.08, 0.07, 0.05
        ]
    })

    st.subheader("Top Influential Features")
    st.bar_chart(chart.set_index("Feature"))

    st.markdown("---")

    st.subheader("Key Insights")

    st.success("""
        - G2 and G1 are strongest predictors  
        - Failures reduce performance  
        - Absences negatively impact grades  
        - Study time improves results  
    """)
