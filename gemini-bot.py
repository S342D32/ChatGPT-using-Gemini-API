import streamlit as st
import os
import google.generativeai as genai

st.title("My Bot")

os.environ['GOOGLE_API_KEY'] = "AIzaSyCqxpCtMJE5xG-L3pClDHn6fNvLF-VlBs4"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Select a model
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me anything"
        }
    ]

# Display chat messages from history
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Function to process and store query
def llm_function(query):
    response = model.generate_content(query)

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Storing the Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )

    # Displaying the messages
    chat_container.empty()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

# Accept user input
query = st.chat_input("What's up?")

# Calling the function when input is provided
if query:
    # Displaying the User Message
    # with st.chat_message("user"):
    #     st.markdown(query)

    llm_function(query)
