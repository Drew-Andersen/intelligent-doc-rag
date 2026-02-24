from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from app.state import GraphState

llm = ChatOpenAI(model="gpt-4o-mini")

def generate(state: GraphState):
    question = state["messages"][-1].content
    context = state.get("context", "")

    prompt = f"""
    Use the following context to answer the question.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return {
        "messages": state["messages"] + [AIMessage(content=response.content)]
    }