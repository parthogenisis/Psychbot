import streamlit as st
import requests
import datetime

st.set_page_config(page_title="🧠 Mental Health Chatbot", layout="centered")
st.sidebar.page_link("main.py", label="⬅️ Go to Home")

st.title("🧠 Mental Health Chatbot")
st.write("Hey, I'm your therapy bot, let's have a chat!")

GROQ_API_KEY = "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"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a therapy chatbot, you should provide therapy and act like a therapist."}
    ]
if "chat_log" not in st.session_state:
    st.session_state.chat_log = ""  # For saving as text

# Function to call Groq
def get_response_from_groq(message_history):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": message_history,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Sorry, there was an error getting a response."

# User Input
user_input = st.text_input("Enter your message:", placeholder="What's on your mind?")
if st.button("Send"):
    if user_input:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.chat_log += f"You: {user_input}\n"

        with st.spinner("Thinking..."):
            response = get_response_from_groq(st.session_state.messages)
        
        # Append bot response
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.chat_log += f"Bot: {response}\n"
    else:
        st.warning("Please enter a message before sending.")

# Display Chat History
st.markdown("### 💬 Chat History")
for msg in st.session_state.messages[1:]:  # Skip system message
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**Bot:** {msg['content']}")

# Save Chat Option
st.markdown("---")
if st.session_state.chat_log.strip():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"soulsync_chat_{timestamp}.txt"
    st.download_button("📥 Download Chat", st.session_state.chat_log, file_name=filename)
