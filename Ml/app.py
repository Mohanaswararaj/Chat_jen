import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from environment
groq_api_key = os.getenv("groq_api_key")

# UI: Page and Sidebar
st.set_page_config(page_title="Chat with Groq Models", layout="centered")
st.title("💬 Ask Your Queries")

st.sidebar.title("Settings")
model = st.sidebar.selectbox(
    'Choose a model',
    ['Llama3-8b-8192', 'Llama3-70b-8192', 'Mixtral-8x7b-32768', 'Gemma-7b-It']
)

# Validate API Key
if not groq_api_key:
    st.error("❌ API key not found. Please set 'groq_api_key' in your .env file.")
    st.stop()

# Init Groq client
client = Groq(api_key=groq_api_key)

# History
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Enter your prompt:")

if st.button("Submit") and user_input.strip() != "":
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model=model,
        )
        response = chat_completion.choices[0].message.content.strip()

        # Save and show response
        st.session_state.history.append({"query": user_input, "response": response})
        st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

# Show history
st.sidebar.title("History")
for i, entry in enumerate(st.session_state.history):
    if st.sidebar.button(f"Query {i+1}: {entry['query']}"):
        st.markdown(f'<div class="response-box">{entry["response"]}</div>', unsafe_allow_html=True)
