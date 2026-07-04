# 🤖 Docchat

Docchat is a local Retrieval-Augmented Generation (RAG) application built with Python. It allows users to upload PDF documents and ask questions based on the document's content.

![Streamlit UI Interface](ui_screenshot.png)

## 🚀 Features
- **Local & Private:** Everything runs locally on your machine using Ollama. No data is sent to external APIs.
- **Fast Vector Search:** Uses Qdrant vector database for lightning-fast document retrieval.
- **Interactive UI:** Clean and easy-to-use Streamlit web interface.
- **Accurate Answers:** Powered by LangChain and Llama 3.2.

## 🛠️ Prerequisites
Before running the application, make sure you have the following installed:
1. **Python 3.9+**
2. **Docker Desktop** (Required for Qdrant Vector DB)
3. **Ollama** (Required for the LLM)
   - Install Ollama and run: `ollama pull llama3.2:latest`

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/docchat.git
   cd docchat
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Qdrant Vector Database:**
   ```bash
   docker run -p 6333:6333 -p 6334:6334 -v qdrant_storage:/qdrant/storage:z qdrant/qdrant
   ```

## 🎯 Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open your browser and go to `http://localhost:8501`.
3. Upload a PDF document using the sidebar.
4. Click **"Create Embeddings"**.
5. Start chatting with your document!

## 🧩 Technologies Used
- **Streamlit**: Web Interface
- **LangChain**: LLM Framework
- **Qdrant**: Vector Database
- **Ollama**: Local LLM Engine (Llama 3.2)
- **HuggingFace**: BGE Embeddings
