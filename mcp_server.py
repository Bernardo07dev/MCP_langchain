from fastmcp import FastMCP

mcp = FastMCP("math-tools")

@mcp.tool()
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

@mcp.tool()
def multiply(arg1: int | float, arg2: int | float) -> int | float:
    """
        This is a tool to multiply 2 numbers, arg1 * arg2

        Args:
            arg1 (int | float): The first number.
            arg2 (int | float): The second number.

        Returns:
            int | float: The product of arg1 and arg2.
    """

    return arg1 * arg2

@mcp.tool()
def divide(arg1: int | float, arg2: int | float) -> int | float:
    """
        This is a tool to divide 2 numbers, arg1 / arg2

        Args:
            arg1 (int | float): The numerator.
            arg2 (int | float): The denominator.

        Returns:
            int | float: The result of dividing arg1 by arg2.
    """

    if arg2 == 0:
        raise ValueError("Cannot divide by zero")

    return arg1 / arg2


if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8000)