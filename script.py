# with open('test-file.txt', 'a') as text:
#     text.write(", isa")


# with open('test-file.txt', 'r') as text:
#     print(text.read())


# per: https://stackabuse.com/python-list-files-in-a-directory/
import pathlib

currentDirectory = pathlib.Path('.')

for filename in currentDirectory.iterdir():
    print (filename)