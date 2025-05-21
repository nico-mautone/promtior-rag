from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import EMBEDDING_MODEL, LLM_MODEL, OPENAI_API_KEY, PERSIST_DIR

_SYSTEM = """You are Promtior's AI assistant. Use ONLY the provided context to answer. Cite sources with [#]."""
template = PromptTemplate(
    input_variables=["context", "question"],
    template=_SYSTEM + "\n\nContext:\n{context}\n\nQuestion: {question}"
)

def build_chain():
    """
    Build a RAG chain.
    First, we load the vector store from the persist directory.
    Then, we create a retriever from that db, that can be used to retrieve the most relevant documents.
    Then, we create a LLM that can be used to answer questions.
    Finally, we create a chain that can be used to answer questions.
    
    Returns:
        ConversationalRetrievalChain: A chain that can be used to answer questions.
    """
    store = Chroma(persist_directory=PERSIST_DIR,
                   embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL,
                                                       api_key=OPENAI_API_KEY))
    retriever = store.as_retriever(search_kwargs={"k":4})
    llm = ChatOpenAI(model=LLM_MODEL, temperature=0.1, api_key=OPENAI_API_KEY)
    return ConversationalRetrievalChain.from_llm(
        llm, retriever, combine_docs_chain_kwargs={"prompt": template}, return_source_documents=True
    )
