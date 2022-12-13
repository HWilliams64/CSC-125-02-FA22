def user_input_number():
    ui = input() # 23
    
    if not ui.strip().replace('-', '').replace('.', '').isdigit():
        print(f'The value "{ui}" is not a valid number')
        return user_input_number()
    else:
        return float(ui.strip())

user_input = user_input_number()
print(user_input)