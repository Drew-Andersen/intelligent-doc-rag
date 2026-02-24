from app.chroma_client import get_retriever
from app.state import GraphState

retriever = get_retriever()

def retrieve(state: GraphState):
    question = state["messages"][-1].content

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    return {
        "context": context
    }