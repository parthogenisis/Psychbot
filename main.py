import streamlit as st
import os

st.set_page_config(page_title="SoulSync AI", layout="centered")

# Hide the sidebar completely using custom CSS
hide_sidebar = """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""

def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    load_css()
    st.markdown(hide_sidebar, unsafe_allow_html=True)  # 👈 Hide sidebar here

    st.markdown('<h1 class="main-heading">SOULSYNC.AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-heading">Select a Feature to Get Started</p>', unsafe_allow_html=True)

    st.markdown("""
        <div class="button-group">
            <a href="/Mental_Health_Chatbot" class="feature-button">🧠 Mental Health Chatbot</a><br>
            <a href="/Hospital_Policy_Formation" class="feature-button">🏥 Hospital Policy Formation</a><br>
            <a href="/Budget_Allocation" class="feature-button">💸 Budget Allocation Tool</a><br>
            <a href="/Symptom_Checker" class="feature-button">🤒 Symptom Checker</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<footer>Made with ❤️ by Parth Gupta</footer>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
