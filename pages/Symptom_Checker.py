import streamlit as st

# Set page config (this must be the first Streamlit command)
st.set_page_config(page_title="Mental Health Chatbot | SoulSync AI", layout="centered")

# Load shared styles
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


st.markdown('<h1 class="main-heading">🤒 Symptom Checker</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-heading">Enter your symptoms, and we’ll give a possible diagnosis (not a substitute for a doctor).</p>', unsafe_allow_html=True)

symptoms = st.text_input("Describe your symptoms", placeholder="E.g. headache, fatigue, fever...")

if symptoms:
    st.warning("🩺 This is a general suggestion only.")
    st.success("💡 Possible Condition: Viral Infection\nRecommendation: Rest, hydration, and consult a physician.")

st.markdown("<footer>Made with ❤️ by Parth Gupta</footer>", unsafe_allow_html=True)
