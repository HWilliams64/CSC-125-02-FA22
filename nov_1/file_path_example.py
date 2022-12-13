from os import path

print('\n'*2)
print(__file__)
print('/etc/fonts/fonts.conf')
print(path.abspath('./'))

file_path = './rejnlegjrnl'
if path.isdir(file_path):
    print('The path is a directory.')

if path.isfile(file_path):
    print('The path is a file.')

if path.exists(file_path):
    print('The path exist')
else:
    print('The path does not exist')
