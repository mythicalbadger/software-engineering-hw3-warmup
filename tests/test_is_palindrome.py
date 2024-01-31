from src.leetcode.is_palindrome import is_palindrome


def test_is_palindrome_empty():
    assert is_palindrome("") is True


def test_is_palindrome_true():
    assert is_palindrome("a") is True
    assert is_palindrome("aba") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("abcba") is True
    assert is_palindrome("abccba") is True
    assert is_palindrome("abcdeedcba") is True


def test_is_palindrome_false():
    assert is_palindrome("ab") is False
    assert is_palindrome("abc") is False
    assert is_palindrome("abca") is False
    assert is_palindrome("abcca") is False
    assert is_palindrome("abcdeedcb") is False
    assert is_palindrome("abcdeedcbax") is False
