from langchain.chat_models import init_chat_model
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

Base_llm = init_chat_model(
    model="openai/gpt-4o",
    model_provider="openai"
)

@tool
def add(arg1: int | float, arg2: int | float) -> int | float:
    """
        This is a tool to add 2 numbers, arg1 + arg2

        Args:
            arg1 (int | float): The first number.
            arg2 (int | float): The second number.

        Returns:
            int | float: The sum of arg1 and arg2.
    """

    return arg1 + arg2

tools = [add]


llm = Base_llm.bind_tools(tools)


