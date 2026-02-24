from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from app.graph import graph
from app.chroma_client import ingest_pdf

ingest_pdf("Foundations_of_Strength_Training.pdf")

config = {"configurable": {"thread_id": "user-1"}}

while True:
    question = input("\nAsk: ")

    result = graph.invoke(
        {"messages": [HumanMessage(content=question)]},
        config=config
    )

    print("\nAnswer: ", result["messages"][-1].content)