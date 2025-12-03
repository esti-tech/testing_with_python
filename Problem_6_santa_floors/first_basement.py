def move_floor(char: str) -> int:
    """
    Returns +1 if '(' else -1 if ')'.
    """
    pass


def first_basement_position(instructions: str) -> int:
    """
    Returns the position where Santa first enters the basement.
    Returns -1 if never enters basement.
    """
    pass


# Main program
if __name__ == "__main__":
    instructions = input("Enter Santa's instructions: ").strip()
    pos = first_basement_position(instructions)
    if pos == -1:
        print("Santa never enters the basement.")
    else:
        print("Santa enters the basement at position:", pos)
