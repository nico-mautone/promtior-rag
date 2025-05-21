from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from config import EMBEDDING_MODEL, OPENAI_API_KEY, PERSIST_DIR

def embed_and_persist(chunks):
    """
    Embed and persist a Chroma vector store.
    
    Args:
        chunks: The document chunks to embed
        
    Returns:
        The vector store instance
    """
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL, api_key=OPENAI_API_KEY)
    vec_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(PERSIST_DIR),
    )
    return vec_store