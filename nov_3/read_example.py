with open('./text_file.txt', 'r') as file:
    print(file.read())
    print('-'*10)
    file.seek(5)
    for line in file:
        print(line.strip())
