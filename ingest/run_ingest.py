from .loaders import load_documents
from .splitter import split_documents
from .embed import embed_and_persist

def main():
    """
        Run the ingestion process to create and persist the vector store.

        This script orchestrates the entire ingestion pipeline:
        1. Load documents from web and PDF sources
        2. Split documents into chunks
        3. Embed chunks and persist to vector store
    """
    # Step 1: Load documents
    web_docs, pdf_docs = load_documents()
    
    # Step 2 & 3: Split documents, embed and persist
    print("Processing documents...")
    all_docs = web_docs + pdf_docs
    chunks = split_documents(all_docs)
    print(f"Created {len(chunks)} chunks from {len(all_docs)} documents")
    
    # Step 4: Embed and persist
    vector_store = embed_and_persist(chunks)
    print(f"Vector store persisted successfully.")

if __name__ == "__main__":
    main() 