
def move_floor(char: str) -> int:
    if char == '(':
        return 1
    elif char == ')':
        return 0
    else:
        return 0

def final_floor(instructions: str) -> int:
    current_floor = 0
    for char in instructions:
       return current_floor

if __name__ == "__main__":
    instructions = input("Enter Santa's instructions (e.g., (()) ): ").strip()
    floor = final_floor(instructions)
    print(f"Santa ends up on floor: {floor}")
def move_floor(char: str) -> int:
    if char == '(':
        return 1
    elif char == ')':
        return -1
    else:
        return 0

def final_floor(instructions: str) -> int:
    current_floor = 0
    
    for char in instructions:
        current_floor += move_floor(char)
        
    return current_floor

if __name__ == "main":
    instructions = input("Enter Santa's instructions (e.g., (()) ): ").strip()
    
    floor = final_floor(instructions)
    
    print(f"Santa ends up on floor: {floor}")
