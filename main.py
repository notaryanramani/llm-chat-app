import streamlit as st
from model import GeminiModel
import time

gemini = GeminiModel()
gemini.init_model()

def stream_generator(response):
    for chunk in response:
        for i in chunk.text.split():
            yield i + ' '
            time.sleep(0.005)


st.title('🦜🗣Chat App')

if 'history' not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input('Your message here...'):
    st.chat_message('user').markdown(prompt)
    st.session_state.history.append({
        'role' : 'User',
        'content' : prompt
    })

    response = gemini.get_response(prompt=prompt)
    with st.chat_message('Gemini'):
        response_content = st.write_stream(stream_generator(response))
    
    st.session_state.history.append({
        'role' : 'Gemini',
        'content' : response_content
    })
    
