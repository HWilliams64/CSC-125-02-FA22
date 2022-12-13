def num_input() -> float:
    ui = input("Type in a number: ")
    try:
        return float(ui)
    except ValueError:
        print(f"The value \"{ui}\" is not a number. Try again.")
        num_input()

num1 = num_input()
num2 = num_input()

print(f"{num1} + {num2}")


# line 9
# line 1 num_input() -> wrong input
# line 7 recursion 
# line 1 num_input() -> correct input
# line 4 return float(ui)
# line 7 recursion
# line 9
