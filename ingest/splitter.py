from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP

def split_documents(documents):
    """
    Split documents into chunks.
    
    Args:
        documents: The documents to split into chunks.
        
    Returns:
        list[Document]: A list of document chunks.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    
    return splitter.split_documents(documents)
