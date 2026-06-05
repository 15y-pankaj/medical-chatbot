# Medical Chatbot

## Overview

This repository implements a medical question-answering chatbot using Flask, LangChain, Pinecone, and Google Generative AI.

The app loads medical PDF documents, embeds document chunks with Hugging Face embeddings, stores them in a Pinecone index, and then performs retrieval-augmented generation to answer user questions.

## Key Components

- `app.py`
  - Main Flask application.
  - Loads environment variables with `python-dotenv`.
  - Uses `PineconeVectorStore` and `GoogleGenerativeAI`.
  - Builds a retrieval-augmented generation chain using LangChain.
  - Serves the chat UI at `/` and responds to `/get` requests.

- `store_index.py`
  - Loads PDF documents from the `data/` folder.
  - Splits documents into chunks using `RecursiveCharacterTextSplitter`.
  - Creates a Pinecone serverless index named `medical-chatbot-index`.
  - Uploads vector embeddings from `sentence-transformers/all-MiniLM-L6-v2`.

- `src/helper.py`
  - Encapsulates PDF loading, text chunking, and Hugging Face embedding creation.
  - Uses `DirectoryLoader`, `PyPDFLoader`, `RecursiveCharacterTextSplitter`, and `HuggingFaceEmbeddings`.

- `src/prompt.py`
  - Defines the system prompt for the medical chatbot.
  - Instructs the model to answer using retrieved context and stay concise.

- `templates/index.html`
  - Chat interface built with Bootstrap and jQuery.
  - Sends user input to the Flask backend and displays bot responses.

- `static/style.css`
  - Custom chat UI styling.

## Dependencies

This project uses the following main packages:

- Flask
- python-dotenv
- langchain
- langchain-core
- langchain-google-genai
- langchain-pinecone
- langchain-community
- langchain-text-splitters
- pinecone
- google-generativeai
- sentence-transformers
- torch

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root with:

```env
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_google_api_key
```

## Running the Project

1. Add your PDF documents into the `data/` folder.
2. Create the Pinecone index and upload embeddings:

```bash
python store_index.py
```

3. Start the Flask app:

```bash
python app.py
```

4. Visit `http://127.0.0.1:8080` in your browser.

## Important Notes

- `store_index.py` currently loads PDF files from an absolute path specific to the local machine. For portability, update the data path to a relative path if needed.
- `store_index.py` creates a Pinecone index using `ServerlessSpec` in the `us-east-1` AWS region.
- `app.py` expects a Pinecone index named `medical-chatbot-index`.
- `app.py` starts the Flask server with `debug=True`; this is suitable for development only.
- The chatbot model is configured to use `gemini-3-flash-preview`.
- `test.py` and `src/__init__.py` are empty placeholder files.
- `template.py` is a helper script that creates missing files/directories, not part of the chatbot runtime.

## Project Structure

- `app.py` - Flask application and chat route.
- `store_index.py` - Index creation, PDF ingestion, and embedding upload.
- `src/helper.py` - Data loading, splitting, and embedding helper functions.
- `src/prompt.py` - Chatbot system prompt.
- `templates/index.html` - Front-end chat UI.
- `static/style.css` - Styling for the chat interface.
- `data/` - Directory for source PDF documents.
- `requirements.txt` - Python package dependencies.
