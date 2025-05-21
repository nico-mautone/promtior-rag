from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    """
    Split documents into chunks.
    
    Args:
        documents: The documents to split into chunks.
        
    Returns:
        list[Document]: A list of document chunks.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=100)
    
    return splitter.split_documents(documents)
