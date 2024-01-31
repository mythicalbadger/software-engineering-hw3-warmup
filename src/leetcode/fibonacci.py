def fibonacci(n: int) -> int:
    """
    Calculate the nth fibonacci number.

    Args:
        n: The nth number to calculate.

    Returns: The nth fibonacci number.

    """
    if n < 0:
        raise ValueError("n must be greater than or equal to 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
