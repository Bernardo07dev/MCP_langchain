from langchain_core.messages import BaseMessage, HumanMessage
from rich.markdown import Markdown
from rich.console import Console

console = Console()

def md_print(text: str):
    return console.print(Markdown(text))

def call() -> BaseMessage:
     msg_user = console.input("[bold cyan]Você: [/bold cyan]")
     return HumanMessage(msg_user)


