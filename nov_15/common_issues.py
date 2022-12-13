import os

if not os.path.isfile('./stuff.txt'):
    raise SystemError('The file ./stuff.txt was not found')