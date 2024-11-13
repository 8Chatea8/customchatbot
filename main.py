import streamlit as st
import chat 
import time
import os 

st.title("커스텀 챗봇 만들기 실습")

option = st.selectbox(
    "대화하고 싶은 캐릭터를 선택해주세요",
    ("해리포터", "슈퍼 마리오", "곰돌이 푸", "기타")
)
if option == "기타":
    character = st.text_input("대화하고 싶은 캐릭터를 입력해주세요")
else:
    character = option

if character:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if prompt := st.chat_input("what's up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response =  chat.get_response(prompt, character)
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
