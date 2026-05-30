import asyncio
from langchain_core.messages import BaseMessage, SystemMessage
from typing import Annotated, TypedDict
import operator
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode
from rich import print
from rich.console import Console
from chatbot_utils import call, md_print
from llm import Base_llm, llm, load_mcp_tools


console = Console()

class State (TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]

def input(state: State) -> dict:
    u_input= call()
    if u_input == "":
        return END
    return {'messages': [u_input]}

def router(state: State) -> dict:
    list_m = state['messages'][-1]
    if getattr(list_m, "tool_calls"):
        console.print(f"[bold yellow]TOOL CALL {list_m.tool_calls[0]['name']} [/bold yellow]")
        return "tool_node"
    md_print(list_m.content)
    return "input"

async def main():
    tools, mcp_client = await load_mcp_tools()
    llm = Base_llm.bind_tools(tools)
    tool_node = ToolNode(tools)

    def llm_call(state: State) -> dict:
        response = llm.invoke(state['messages'])
        return {'messages': [response]}

    builder = StateGraph(State)
    builder.add_node("input", input)
    builder.add_node("llm_call", llm_call)
    builder.add_node("tool_node", tool_node)
    builder.set_entry_point("input")
    builder.add_edge("input", "llm_call")
    builder.add_edge("tool_node", "llm_call")
    builder.add_conditional_edges("llm_call", router, ["tool_node", "input"])

    graph = builder.compile()
    S_M = SystemMessage("Você é uma IA de matemática, de respostas curtas" "VOCE TEM ACESSO A TOOLS, " \
    "SEMPRE QUE FOR FAZER ALGO MATEMATICO, USE-AS")

    await graph.ainvoke({"messages": [S_M]})

asyncio.run(main())

