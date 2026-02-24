from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver 
from app.state import GraphState
from app.nodes.retrieve import retrieve
from app.nodes.generate import generate
import sqlite3

# Builds the base graph once
builder = StateGraph(GraphState)

builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)
builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

def get_graph(thread_id: str):
    conn = sqlite3.connect("langgraph_checkpoint.db", check_same_thread=False)
    saver = SqliteSaver(conn=conn)

    return builder.compile(checkpointer=saver)