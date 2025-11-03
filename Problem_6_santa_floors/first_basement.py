"""
🎅 Santa Floors — Part Two

Now, using the same instructions:
Find the position of the first character that causes Santa to enter the basement (floor -1).
The first character has position 1, the second has position 2, and so on.
"""

def move_floor(ch: str) -> int:
    """Returns +1 if '(' else -1 if ')'."""
    if ch == '(':
        return 1
    elif ch == ')':
        return -1
    return 0


def first_basement_position(instructions: str) -> int:
    """Finds the first position where Santa enters the basement."""
    floor = 0
    for i, ch in enumerate(instructions, start=1):
        floor += move_floor(ch)
        if floor < 0:
            return i
    return -1


if __name__ == "__main__":
    instructions = input("Enter Santa's instructions: ").strip()
    pos = first_basement_position(instructions)
    if pos == -1:
        print("🎁 Santa never enters the basement.")
    else:
        print("🎅 Santa enters the basement at position:", pos)
