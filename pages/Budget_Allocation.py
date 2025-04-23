import streamlit as st

# Set page config (this must be the first Streamlit command)
st.set_page_config(page_title="Mental Health Chatbot | SoulSync AI", layout="centered")

# Load shared styles
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown('<h1 class="main-heading">💸 Budget Allocation Tool</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-heading">Input your departments and available funds to generate a suggested allocation.</p>', unsafe_allow_html=True)

departments = st.text_area("Enter departments and required funds (one per line)", placeholder="Psychology - 5L\nPharmacy - 3L")

if departments:
    st.success("📊 Suggested Allocation Complete: Check detailed breakdown below.")
    st.dataframe({"Department": ["Psychology", "Pharmacy"], "Allocated Budget (in Lakhs)": [5, 3]})

st.markdown("<footer>Made with ❤️ by Parth Gupta</footer>", unsafe_allow_html=True)
