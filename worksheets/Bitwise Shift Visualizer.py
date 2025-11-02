"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
def bitwise_shift_visualizer():
    # Input an integer and number of shift positions

    try:
        # Get an number and number of shift 
        number = int(input("Input an integer: "))
        shifts = int(input("Input number of shift positions: "))

        # Print the original number and its binary representation
        print(f"\nOriginal Number: {number}")
        print(f"Binary: {bin(number)}")

        # Perform and show the results of a left shift
        left_shifted = number << shifts
        print(f"\nLeft Shift by {shifts} positions:")
        print(f"Decimal result: {left_shifted}")
        print(f"Binary: {bin(left_shifted)}")

        # Perform and show the results of a right shift
        right_shifted = number >> shifts
        print(f"\nRight Shift by {shifts} positions:")
        print(f"Decimal result: {right_shifted}")
        print(f"Binary: {bin(right_shifted)}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    bitwise_shift_visualizer()