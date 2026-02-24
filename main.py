from dotenv import load_dotenv
load_dotenv()

import uuid
from langchain_core.messages import HumanMessage
from app.graph import get_graph
from app.chroma_client import ingest_pdf

# ingest_pdf("Foundations_of_Strength_Training.pdf")

thread_id = str(uuid.uuid4())
graph = get_graph(thread_id)

while True:
    question = input("\nAsk: ")
    if question.lower() in ["exit", "quit"]:
        break

    config = {"thread_id": thread_id}

    result = graph.invoke(
        {"messages": [HumanMessage(content=question)]},
        config=config
    )

    print("\nAnswer: ", result["messages"][-1].content)