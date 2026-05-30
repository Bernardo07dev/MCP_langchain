from langchain.messages import SystemMessage
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from graph import State, llm_call, router
from llm import Base_llm, llm, load_mcp_tools
import asyncio

# if __name__ == "__main__":
#     print(llm.invoke("Some 5 + 10"))
