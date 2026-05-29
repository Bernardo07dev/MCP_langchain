from langchain_core.messages import BaseMessage, SystemMessage
from typing import Annotated, TypedDict
import operator
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode
from rich import print
from rich.console import Console
from llm import tools, llm
from chatbot_utils import call, md_print


console = Console()

class State (TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]

tool_node = ToolNode(tools)

def input(state: State) -> dict:
    u_input= call()
    if u_input == "":
        return END
    return {'messages': [u_input]}

def llm_call(state: State) -> dict:
    response = llm.invoke(state['messages'])
    return {'messages': [response]}

def router(state: State) -> dict:
    list_m = state['messages'][-1]
    if getattr(list_m, "tool_calls"):
        console.print(f"[bold yellow]TOOL CALL[/bold yellow]")
        return "tool_node"
    md_print(list_m.content)
    return "input"

builder = StateGraph(State)
builder.add_node("input", input)
builder.add_node("llm_call", llm_call)
builder.add_node("tool_node", tool_node)
builder.set_entry_point("input")
builder.add_edge("input", "llm_call")
builder.add_edge("tool_node", "llm_call")
builder.add_conditional_edges("llm_call", router, ["tool_node", "input"])

graph = builder.compile()
S_M = SystemMessage("Você é uma IA de matemática, de respostas curtas" \
"VOCE TEM ACESSO A TOOLS, SEMPRE QUE FOR FAZER ALGO MATEMATICO, USE-AS" \
"")
graph.invoke({"messages": [S_M ]})



