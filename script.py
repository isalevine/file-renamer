# with open('test-file.txt', 'a') as text:
#     text.write(", isa")


# with open('test-file.txt', 'r') as text:
#     print(text.read())




# per: https://stackabuse.com/python-list-files-in-a-directory/
import pathlib

# GOAL: create CLI to navigate & select directory,
# set Regex/string-matching for filenames, and
# replace (look for GSUB equivalent?) with specified text
path = './drum-samples'

currentDirectory = pathlib.Path(path)

currentDirectory = currentDirectory / "SDS800 Kits"

for filename in currentDirectory.iterdir():
    print (filename)

input = input("Enter directory name: ")
print("Directory name chosen: " + input)

# print(type(currentDirectory))

if (currentDirectory / input).exists():
    print("true!!")