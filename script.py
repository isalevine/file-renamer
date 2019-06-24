# with open('test-file.txt', 'a') as text:
#     text.write(", isa")


# with open('test-file.txt', 'r') as text:
#     print(text.read())




# GOAL: create CLI to navigate & select directory,
# set Regex/string-matching for filenames, and
# replace (look for GSUB equivalent?) with specified text


# currentDirectory = currentDirectory / "SDS800 Kits"

# for filename in currentDirectory.iterdir():
#     print (filename)

# input = input("Enter directory name: ")
# print("Directory name chosen: " + input)

# # print(type(currentDirectory))

# if (currentDirectory / input).exists():
#     print("true!!")




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




# per: https://stackabuse.com/python-list-files-in-a-directory/
import pathlib

path = './drum-samples'

currentDirectory = pathlib.Path(path)



def print_menu():
    global currentDirectory

    menu_text = """
    Hello, and welcome to Filename Reader!
    
    This handy CLI is designed for mass-renaming
    of drum sample filenames, specifically from
    Samples From Mars downloads.

    ~~~

    """
    
    # print_current_directory()
    print(menu_text)
    user_input = ""

    while user_input != "quit":
        user_input = get_user_input()
        # print("User input is: " + input)

        if user_input == "dir":
            print_current_directory()

        if user_input == "ls":
            for filename in currentDirectory.iterdir():
                print(filename)

        if user_input[0] == "/":
            currentDirectory = currentDirectory / user_input[1:]
            print_current_directory()
        
        input("")


def print_current_directory():
    print("Current directory is: " + str(currentDirectory))


def get_user_input():
    return input("Enter command: ")



print_menu()