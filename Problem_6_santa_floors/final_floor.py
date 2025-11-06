"""
Santa Floors — Part One

Given a string of parentheses:
- '(' means go up one floor (+1)
- ')' means go down one floor (-1)

Calculate the final floor number Santa ends up on.
"""


def move_floor(char: str) -> int:
    """
    Returns +1 if '(' else -1 if ')'.
    """
    if char =='(':
        return 1
    else:
        return -1


def final_floor(instructions: str) -> int:
    """
    Calculates the final floor Santa ends on.
    """
    floor=0
    for char in instructions:
        floor+= move_floor(char)
    return floor


# --- Main Program ---
if __name__ == "__main__":
    instructions = input("Enter Santa's instructions (e.g. (()()) ): ").strip()
    floor = final_floor(instructions)
    print("Santa ends up on floor:", floor)
