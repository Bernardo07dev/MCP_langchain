from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from rich import console, print
from rich.console import Console
from rich.markdown import Markdown

console = Console()


load_dotenv()

def main():
    print("Hello from mcp-langchain!")

def md_print(text: str):
    return console.print(Markdown(text))


# llm = init_chat_model(
#     model="perceptron/perceptron-mk1",
#     model_provider="openai"
# )

# print(llm.invoke("Olá IA"))

if __name__ == "__main__":
    main()
