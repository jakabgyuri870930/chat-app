import streamlit as st
from google import genai
from google.genai import types
from datetime import datetime

# 1. THE PASSWORD BOUNCER
password = st.text_input("Enter Password:", type="password")

if password != "mysecret123":
    st.warning("Please enter the password to access the AI.")
    st.stop()

# 2. APP HEADER
st.title("🤖 My Personal AI")
st.write("Welcome to your private chat room!")

# 3. THE BACKPACK (Session State Memory)
if "chat_session" not in st.session_state:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    today = datetime.now().strftime("%B %d, %Y")
    bot_rules = f"You are a helpful, friendly AI assistant. You talk to the client like you are a female friend. Today is {today}."

    st.session_state.chat_session = client.chats.create(
        model='gemini-2.5-flash',
        config=types.GenerateContentConfig(system_instruction=bot_rules)
    )
    st.session_state.messages = []

# 4. DRAW THE PREVIOUS MESSAGES
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 5. NEW USER INPUT
user_message = st.chat_input("Type your message here...")

if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    st.session_state.messages.append({"role": "user", "content": user_message})

    try:
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.write(response.text)
        st.session_state.messages.append(
            {"role": "assistant", "content": response.text})

    except Exception as error_message:
        st.error(f"Connection glitch: {error_message}")
