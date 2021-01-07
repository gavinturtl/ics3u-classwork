# Exercise 87:

def main():
    string = input("Enter a string: ")

    while True:
        try:
            width = int(input("Enter the width of the terminal: "))
            if width < 1:
                raise ValueError
            break
        except ValueError:
            "Invalid width."
    
    result = center_string(string, width)
    print(result)


def center_string(string: str, width: int) -> str:
    left_spaces = (width - len(string)) // 2
    centered_string = " " * left_spaces + string
    return centered_string


def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    print("all passed!")


if __name__ == "__main__":
    tests()
    main()
