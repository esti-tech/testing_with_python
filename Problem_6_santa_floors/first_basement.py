def move_floor(char: str) -> int:
    """
    Returns +1 if '(' else -1 if ')'.
    """
    
    if char == '(':
        return 1
    elif char == ')':
        return -1
    else:
        return 0


def first_basement_position(instructions: str) -> int:
    """
    Returns the position where Santa first enters the basement.
    Returns -1 if never enters basement.
    """
    
    floor = 0
    index = 0
    for char in instructions:
        index += 1
        floor += move_floor(char)
        if floor == -1:
            return index
    return -1
        

# Main program
if __name__ == "__main__":
    instructions = input("Enter Santa's instructions: ").strip()
    pos = first_basement_position(instructions)
    if pos == -1:
        print("Santa never enters the basement.")
    else:
        print("Santa enters the basement at position:", pos)
