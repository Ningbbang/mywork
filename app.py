import openai
import streamlit as st

promt = st.chat_input('ask something')

openai.api_key "api_key"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": promt}
    ]
)
# st.chat_message(response['choices'][0]['message']['content'])
try:
    st.write(response['choices'][0]['message']['content'])
except:
    st.write('no prompt input')