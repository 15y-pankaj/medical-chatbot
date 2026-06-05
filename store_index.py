from src.helper import load_pdf_file, text_splitter, download_huggingface_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


extracted_data = load_pdf_file(r"C:\Users\visha\OneDrive\Project\medical-chatbot\data")
text_chunks = text_splitter(extracted_data)
embeddings = download_huggingface_embeddings()

pc = Pinecone(api_key = PINECONE_API_KEY)

index_name = "medical-chatbot-index"

pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec = ServerlessSpec(
                cloud = 'aws',
                region = 'us-east-1',

          )
     )

# Embed each chunk and upsert the embeddings into your Pinecone index

dosearch = PineconeVectorStore(
    index_name=index_name,
    embedding = embeddings
)
dosearch.add_documents(text_chunks)
