# app.py
import streamlit as st
import time
import base64
from vectors import EmbeddingsManager
from chatbot import ChatbotManager

def displayPDF(file):
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

if 'temp_pdf_path' not in st.session_state:
    st.session_state['temp_pdf_path'] = None
if 'chatbot_manager' not in st.session_state:
    st.session_state['chatbot_manager'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.set_page_config(page_title="Docchat", layout="wide")

st.title("🤖 Docchat")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("📂 Upload Document")
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file is not None:
        st.success("📄 File Uploaded!")
        displayPDF(uploaded_file)
        
        temp_pdf_path = "temp.pdf"
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state['temp_pdf_path'] = temp_pdf_path

with col2:
    st.header("🧠 Embeddings")
    if st.button("✅ Create Embeddings"):
        if st.session_state['temp_pdf_path'] is None:
            st.warning("⚠️ Please upload a PDF first.")
        else:
            with st.spinner("🔄 Embeddings are in process..."):
                embeddings_manager = EmbeddingsManager()
                result = embeddings_manager.create_embeddings(st.session_state['temp_pdf_path'])
                st.success(result)
                
                st.session_state['chatbot_manager'] = ChatbotManager()

with col3:
    st.header("💬 Chat with Document")
    if st.session_state['chatbot_manager'] is None:
        st.info("🤖 Upload a PDF and create embeddings first.")
    else:
        for msg in st.session_state['messages']:
            st.chat_message(msg['role']).markdown(msg['content'])

        if user_input := st.chat_input("Type your message here..."):
            st.chat_message("user").markdown(user_input)
            st.session_state['messages'].append({"role": "user", "content": user_input})

            with st.spinner("🤖 Responding..."):
                answer = st.session_state['chatbot_manager'].get_response(user_input)
            
            st.chat_message("assistant").markdown(answer)
            st.session_state['messages'].append({"role": "assistant", "content": answer})
