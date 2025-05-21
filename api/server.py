from fastapi import FastAPI
from langserve import add_routes
from chains.rag_chain import build_chain

app = FastAPI(title="Promtior Chatbot")
rag_chain = build_chain()

add_routes(
    app,
    rag_chain,
    path="/chat",
)
