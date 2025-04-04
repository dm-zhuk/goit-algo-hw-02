from collections import deque


def is_palindrome(input_string):
    d = deque()

    cleaned_string = input_string.lower().replace(" ", "")

    # If string is empty or character=1, it's a palindrome
    if len(cleaned_string) <= 1:
        return True
    for char in cleaned_string:
        d.append(char)

    # Compare characters from both ends
    while len(d) > 1:
        left_char = d.popleft()
        right_char = d.pop()

        if left_char != right_char:
            return False

    return True


def test_palindrome_checker():
    test_cases = [
        "hello",
        " racecar ",
        " carrace ",
        "aBBa",
        "aBaLaGaMa",
        "a",
        "",
    ]

    for test in test_cases:
        result = is_palindrome(test)
        print(f"On test: '{test}'")
        print(f"Is a palindrome? {result}\n")


if __name__ == "__main__":
    test_palindrome_checker()
