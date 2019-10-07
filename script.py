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



# CONSIDER ADDING A MAIN MENU WITH SEVERAL OPTIONS:
# 1. set default path
# 2. toggle arrow function syntax for commands (rn all Snare => Snr)...anything different it can do?
#       (...or just make it an optional way of entering commands...)
#       alt: consider implementing "" to denote whitespace... (rn all "Snare " "Snr")
#       or: arrow functions could encapsulate multiple changes? : ("Example 1", "Example 2") => ("ex1", "ex2")
# 3. toggle logging of filename changes => could this possibly lead to an undo function??
# 4. help/instructions
# 5. exit
#
# OTHER ADD-ONS:
# - be able to select individual files and do more with them? (i.e. see/edit metadata?)
# - have a slick CLI interface that can constantly show/update the directory's files? (toggle??)



# per: https://stackabuse.com/python-list-files-in-a-directory/
import pathlib
# per: https://stackoverflow.com/questions/54152653/renaming-file-extension-using-pathlib-python-3
import os


path = os.path.realpath('./drum-samples')   # set default path here
current_directory = pathlib.Path(path)


# call once, then store in memory somewhere? (currently not used!!)
def enter_filepath():
    text = "Please enter your default path: (Empty will result in './')"
    print(text)
    user_input = get_user_input()


def print_menu():
    global current_directory

    menu_text = """
    Hello, and welcome to Filename Reader!
    
    This handy CLI is designed for mass-renaming
    of drum sample filenames, specifically from
    Samples From Mars downloads.

    ~~~"""
    
    # print_current_directory()
    print(menu_text)
    user_input = ""

    # more efficient way to iterate through checks for q/quit, y/yes, etc?
    while (user_input != "quit") and (user_input != "q"):
        user_input = get_user_input()
        # print("User input is: " + input)

        if user_input == "pwd":
            print_current_directory()

        if user_input == "ls":
            for filename in current_directory.iterdir():
                print(filename)

        if user_input == "h" or user_input == "help":   # currently empty - use Readme text!
            print_help_menu()

        # rn = rename ... anything better to use??
        if user_input[0:2] == "rn":
            array = user_input.split(" ")

            if array[1] == "\\all":
                array[1] = "all"

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
                    array[3] = ""


                # MUST be a way to only iterate through current_directory once!!
                # => think about it then refactor...! (type: PosixPath)
                print("You are going to replace: " + array[2] + " => " + array[3])
                print("This will affect the following files: ")
                for filename in current_directory.iterdir():
                    if array[2] in str(filename):
                        print(filename)
                print("Do you want to proceed? (Y/n)")
                final_check = get_user_input()

                if (final_check == "Y") or (final_check == "y") or (final_check == "Yes") or (final_check == "yes"):
                    print("Files changed:")
                    for filename in current_directory.iterdir():
                        if array[2] in str(filename):
                            dst = rename_partial_filename(filename, array[2], array[3])
                            print(dst)
                else:
                    print("Rename aborted!")
                    continue

            else:  
                if array[1] and array[2] and os.path.isfile(array[1]):
                    rename_whole_filename(array[1], array[2])
                else:
                    print("Rename aborted! (Probably because the original filename wasn't found.)")


        # change the following to cd commands => call a separate
        # cd() function that parses and changes current_directory?

        # REFACTOR using os.path module!!!
        if user_input[0:2] == "cd":
            temp_directory = current_directory
        
            if user_input[3:5] == "..":
                new_path = current_directory.parent
                current_directory = pathlib.Path(new_path)
            else:
                new_path = os.path.join(current_directory, user_input[3:])
                current_directory = pathlib.Path(new_path)

            print_current_directory()


        if not os.path.isdir(current_directory):
            print("Not a valid directory!")
            current_directory = temp_directory


def print_current_directory():
    print("Current directory is: " + str(current_directory))


def get_user_input():
    print("")
    return input("Enter command: ")


def rename_whole_filename(filename1, filename2):
    src = filename1
    dst = filename2
    os.rename(src, dst)


def rename_partial_filename(filename, input, output):
    # per: https://stackoverflow.com/a/3675423
    #
    # note: this does NOT solve issue of replacing strings in parent 
    # directory names if no match is found in a given file...
    # (i.e. try replacing SDS800 with \ inside any sample folder)
    #
    src = str(filename)
    head, sep, tail = src.rpartition(input)
    dst = head + output + tail
    os.rename(src, dst)
    return dst


def print_help_menu():
    help_menu = """
        Hi, and welcome to the help menu!

        Commands:
    """

    print(help_menu)


print_menu()