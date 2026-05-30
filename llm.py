import asyncio
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from rich import print

load_dotenv()

Base_llm = init_chat_model(
    model="openai/gpt-4o",
    model_provider="openai"
)

tools = []

async def load_mcp_tools():
    client = MultiServerMCPClient({
        "math": {
            "url": "http://127.0.0.1:8000/sse",
            "transport": "sse",
        }
    })
    tools = await client.get_tools()
    return tools, client


tools, mcp_client = asyncio.run(load_mcp_tools())
llm = Base_llm.bind_tools(tools)
