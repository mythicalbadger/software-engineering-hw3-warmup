def is_palindrome(s: str) -> bool:
    """
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Args:
        s: The string to check.

    Returns: Whether the string is a palindrome or not.

    """
    s = "".join([c for c in s if c.isalnum()]).lower()
    return s == s[::-1]
