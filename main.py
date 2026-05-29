from rich import console, print
from rich.console import Console
from rich.markdown import Markdown
from llm import llm

if __name__ == "__main__":
    print(llm.invoke("Some 5 + 10"))
