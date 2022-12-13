sentence = "Hello my car is red and my shoes are blue"
sub_string = sentence[::-2]

for char in sub_string:
    if char == 'a':
        char = char.upper()
    print(char, end="")