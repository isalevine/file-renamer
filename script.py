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


# IDEA for CLI TO NAVIGATE DIRECTORY:
# -> recursively call an update_directory() function
#    that will append/mutate based on user input, and
#    automatically call the print_menu() function again
# -> once a given directory is selected/"locked in",
#    have user input a string to match (i.e. "Snare")
#    and confirm a list of matching files
# -> then, specify the mutation with a CLI command:
#    $ replace "Snare " with ""
#    and take the first "" and second "" as parameters
#    for calling change_filenames(list, string1, string2)