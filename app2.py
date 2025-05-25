from google import genai
import streamlit as st

prompt = st.chat_input('ask something')

api_key = 'AIzaSyC8Scb2KnVjSTtgPXA0klt1IRZlzouT3YQ'
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

# print(response.text)
try:
    st.write(response.text)
except:
    st.write('no prompt input')