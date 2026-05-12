import streamlit as st

st.set_page_config(page_title="Fake News Detector")

st.title("📰 Fake News Detection System")

st.write("Enter a news headline or statement below:")

text = st.text_area("News Text")

if st.button("Predict"):

    if "miracle cure" in text.lower() or "government hiding" in text.lower():
        st.error("🚨 Prediction: FAKE NEWS")
    else:
        st.success("✅ Prediction: REAL NEWS")
