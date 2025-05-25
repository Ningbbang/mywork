import openai
import streamlit as st

promt = st.chat_input('ask something')

openai.api_key = "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"
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