import streamlit as st
import numpy as np
import pickle

with open("model/rf_model.pkl", "rb") as file:
    model = pickle.load(file)

def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    load_css("static/styles.css")
    st.image("assets/uss_banner.jpg", use_container_width=True)
    st.title("USS Wait Time Predictor")
    st.write("Enter the feature values below to get the predicted wait time:")

    mean_temp = st.slider("Mean Temperature (°C)", min_value=10.0, max_value=40.0, step=0.5, value=30.0)
    is_raining = st.selectbox("Is it raining?", ["No", "Yes"])
    is_weekend = st.selectbox("Is it a weekend?", ["No", "Yes"])
    is_holiday = st.selectbox("Is it a holiday?", ["No", "Yes"])
    is_special_event = st.selectbox("Is there a special event?", ["No", "Yes"])
    international_tourists = st.number_input("Number of International Tourists", min_value=0, value=1000000, step=1)

    is_raining = 1 if is_raining == "Yes" else 0
    is_weekend = 1 if is_weekend == "Yes" else 0
    is_holiday = 1 if is_holiday == "Yes" else 0
    is_special_event = 1 if is_special_event == "Yes" else 0

    features = np.array([[
        mean_temp, is_raining, is_weekend, is_holiday,
        is_special_event, international_tourists
    ]])

    if st.button("Predict Wait Time"):
        prediction = model.predict(features)[0]
        
        if prediction < 20:
            css_class = "low-wait-time"
        elif 20 <= prediction <= 40:
            css_class = "medium-wait-time"
        else:
            css_class = "high-wait-time"

        st.markdown(
            f'<div class="{css_class}">Predicted Wait Time: {prediction:.2f} minutes</div>',
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()
