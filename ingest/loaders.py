from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

from config import PROMTIOR_URLS, PROMTIOR_PDF

def load_documents():
    """
    Load documents from web pages and PDF files.
    First, we load the web documents from the PROMTIOR_URLS.
    Then, we load the PDF documents from the PROMTIOR_PDF.
    
    Returns:
        tuple[list[Document], list[Document]]: A tuple containing the web and PDF documents.
    """
    web_docs = WebBaseLoader(PROMTIOR_URLS).load()
    print(f"Loaded {len(web_docs)} web documents")
    print(web_docs)
    
    pdf_docs = PyPDFLoader(PROMTIOR_PDF).load()
    print(f"Loaded {len(pdf_docs)} PDF documents")
    
    print(f"Loaded {len(web_docs)} web documents and {len(pdf_docs)} PDF documents")
    
    return web_docs, pdf_docs

if __name__ == "__main__":
    load_documents()