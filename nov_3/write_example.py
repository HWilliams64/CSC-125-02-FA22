
with open('./my_notes.txt', 'a') as file:
    while True:
        new_text = input('Please types something: ')
        if not new_text.strip():
            break
        file.write(new_text+'\n')
        file.flush()
        print(f'The text "{new_text}" was saved')


# REPL
# Read
# Event
# Print
# Loop