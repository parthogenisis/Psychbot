import streamlit as st

# Set page config (this must be the first Streamlit command)
st.set_page_config(page_title="Mental Health Chatbot | SoulSync AI", layout="centered")

# Load shared styles
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


st.markdown('<h1 class="main-heading">🏥 Hospital Policy Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-heading">Need help drafting policies for your hospital? Let’s collaborate.</p>', unsafe_allow_html=True)

topic = st.text_input("Enter policy topic (e.g. emergency handling, privacy)")

if topic:
    st.info(f"📄 Drafting policy framework for: **{topic}**")
    st.success("✔️ Generated Sample Policy: All patient data must be encrypted and access restricted to certified personnel only.")

st.markdown("<footer>Made with ❤️ by Parth Gupta</footer>", unsafe_allow_html=True)
