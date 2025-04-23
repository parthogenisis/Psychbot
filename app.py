import streamlit as st
from groq import Groq
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

def main():
    """
    This function is the main entry point of the application. It sets up the Groq client, the Streamlit interface, and handles the chat interaction.
    """

    # Set page layout to wide to remove the sidebar
    st.set_page_config(layout="wide")

    # Get Groq API key
    groq_api_key = "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"

    # Add CSS for custom styling
    st.markdown(
        """
        <style>
       
        .chat-header {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            color: #333;
            margin-bottom: 10px;
        }
        .user-message {
            background-color: #add8e6; /* Light blue */
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            color: #000;
        }
        .ai-message {
            background-color: #ffffff; /* White */
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            color: #000;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .chat-input {
            border: 1px solid #007BFF;
            border-radius: 5px;
            padding: 10px;
            width: 100%;
            box-shadow: 0 2px 4px rgba(0, 123, 255, 0.2);
        }
        .model-selection {
            position: absolute;
            top: 10px;
            left: 10px;
            display: flex;
            align-items: left;
            z-index: 1;
        }
        .slider-container {
            position: absolute;
            top: 10px;
            left: 160px;
            display: flex;
            align-items: center;
        }
        .soul-sync-text {
            font-size: 90px;
            font-weight: bold;
            text-align: center;
            color: #007BFF;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Wrap the main content in a container
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        # Add the "SOULSYNC.AI" text centered at the top
        st.markdown('<div class="soul-sync-text">SOULSYNC.AI</div>', unsafe_allow_html=True)

        # Set a fixed system prompt
        system_prompt = "You are a therapy chatbot and act as a therapy chatbot, give accurate therapeutic advice"

        # Model selection dropdown and arrow button side by side
        model = st.selectbox(
            'Model',
            ['llama3-8b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it'],
            key='model_select',
            label_visibility='collapsed',  # Hide label for compact design
            format_func=lambda x: x[:10]  # Shorten the displayed model name
        )

        # Memory length slider hidden behind an arrow
        if st.button('▼', key='memory_toggle'):
            conversational_memory_length = st.slider('Memory length:', 1, 10, value=5, key='memory_slider')
        else:
            conversational_memory_length = 5  # Default value when slider is hidden

        memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

        # User input box
        user_question = st.text_input("Ask a question:", key='input', placeholder="Type your question here...", 
                                      label_visibility='collapsed')

        # Session state variable
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        # Initialize Groq Langchain chat object and conversation
        groq_chat = ChatGroq(
            groq_api_key=groq_api_key, 
            model_name=model
        )

        # If the user has asked a question,
        if user_question:
            # Display header and greeting message
            ##st.header("Chat with Parth!")
            st.write("Hello! I'm your friendly Parth chatbot. I can help answer your questions, provide information, or just chat. I'm also super fast! Let's start our conversation!")

            # Construct a chat prompt template using various components
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(
                        content=system_prompt
                    ),  # This is the persistent system prompt that is always included at the start of the chat.

                    MessagesPlaceholder(
                        variable_name="chat_history"
                    ),  # This placeholder will be replaced by the actual chat history during the conversation. It helps in maintaining context.

                    HumanMessagePromptTemplate.from_template(
                        "{human_input}"
                    ),  # This template is where the user's current input will be injected into the prompt.
                ]
            )

            # Create a conversation chain using the LangChain LLM (Language Learning Model)
            conversation = LLMChain(
                llm=groq_chat,  # The Groq LangChain chat object initialized earlier.
                prompt=prompt,  # The constructed prompt template.
                verbose=True,   # Enables verbose output, which can be useful for debugging.
                memory=memory,  # The conversational memory object that stores and manages the conversation history.
            )

            # The chatbot's answer is generated by sending the full prompt to the Groq API.
            response = conversation.predict(human_input=user_question)
            message = {'human': user_question, 'AI': response}
            st.session_state.chat_history.append(message)

            # Display chat history
            for msg in st.session_state.chat_history:
                st.markdown(f'<div class="user-message">*You:* {msg["human"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="ai-message">*Chatbot:* {msg["AI"]}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # Close the container

if __name__ == "__main__":
    main()
