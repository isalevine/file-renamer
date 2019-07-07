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
# per: https://stackoverflow.com/questions/54152653/renaming-file-extension-using-pathlib-python-3
import os

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

        # rn = rename ... anything better to use??
        if user_input[0:2] == "rn":
            array = user_input.split(" ")
            if array[1] == "all":
                if (not array[2]) or (not array[3]):
                    print("Rename error!")
                    continue

                # may need to detect empty strings to do beginning inserts?
                # ALSO: may want to ask to confirm empty string inserts?
                if array[2] == '\\':
                    array[2] = ""
                if array[3] == '\\':
                    # use this to count a number of possible blank spaces?
                    array[3] = " "

                for filename in currentDirectory.iterdir():
                    if array[2] in str(filename):
                        print(filename)
                        # next: split filename string, do replacement,
                        # re-concatenate, and call os.rename(str, dst)
            else:  
                # refactor as renaming_function(array[1], array[2]) 
                if array[1] and array[2]:
                    src = array[1]
                    dst = array[2]
                    os.rename(src, dst)
            print("Rename detected!")


        # change the following to cd commands => call a separate
        # cd() function that parses and changes currentDirectory?
        if user_input[0:2] == "cd":
            tempDirectory = currentDirectory
        
            if user_input[3:5] == "..":
                array = str(currentDirectory).split('/')
                print("Current array is: ")
                # print(array)
                del array[-1]
                print(array)
                currentDirectory = "".join(array)
                print(currentDirectory)

            else:
                currentDirectory = currentDirectory / user_input[3:]
                print_current_directory()
        
        # necessary to reset str() of path into a Posix.path object??
        if type(currentDirectory) == str:
            currentDirectory = pathlib.Path("./" + currentDirectory)

        if not os.path.isdir(currentDirectory):
            print("Not a valid directory!")
            currentDirectory = tempDirectory
        
        # input("")


def print_current_directory():
    print("Current directory is: " + str(currentDirectory))


def get_user_input():
    return input("Enter command: ")



print_menu()