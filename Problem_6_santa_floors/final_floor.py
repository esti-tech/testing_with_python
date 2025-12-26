"""
🎅 Santa Floors — Part One

Santa starts on the ground floor (floor 0).
'(' means go up one floor (+1)
')' means go down one floor (-1)

Calculate the final floor number Santa ends up on.
"""

def move_floor(ch: str) -> int:
    """Returns +1 if '(' else -1 if ')'."""
    if ch == '(':
        return 1
    elif ch == ')':
        return -1
    return 0


def final_floor(instructions: str) -> int:
    """Calculates the final floor Santa ends on."""
    return sum(move_floor(ch) for ch in instructions)


if __name__ == "__main__":
    instructions = input("Enter Santa's instructions (e.g. (()()) ): ").strip()
    floor = final_floor(instructions)
    print("🎄 Santa ends up on floor:", floor)
