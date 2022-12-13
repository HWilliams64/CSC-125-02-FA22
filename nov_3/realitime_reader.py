from time import sleep
with open('./my_notes.txt') as file:

    while True:
        text = file.read()
        if text.strip() == 'EXIT':
            print('Someone told me to quit :(')
            break
        if text:
            print(text)
        sleep(.5)
