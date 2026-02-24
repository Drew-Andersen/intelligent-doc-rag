from langgraph.graph import StateGraph, START, END
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver 
from app.state import GraphState
from app.nodes.retrieve import retrieve
from app.nodes.generate import generate

conn = sqlite3.connect("langgraph_checkpoint.db", check_same_thread=False)

builder = StateGraph(GraphState)

builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

memory = SqliteSaver(conn=conn)

graph = builder.compile(checkpointer=memory)