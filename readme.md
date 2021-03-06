# File Renamer
A Python CLI for renaming single and multiple files. Designed to format sample filenames for drum machines, but you can use it for whatever kind of files you want! :)

![gif of file-renamer in action, showing file names as they change](file-renamer-demo.gif)

**NOTE: Default directory is currently set to a _.gitignore_-ed folder of drum samples. [Make sure to update this in order to avoid errors!](https://github.com/isalevine/file-renamer/blob/0e9e2783b0e967433e40820c6fbe7f7d7759c571/script.py#L7)**

Read more about the project in [this article on Dev.to](https://dev.to/isalevine/need-to-rename-files-in-bulk-here-s-a-python-cli-called-file-renamer-2l8m)!

## Highlights
### 1. This is the first Python code I've ever written!
The initial code to navigate the filesystem and rename individual files was written over a two-day period, which included learning Python from scratch.

I was especially excited to dive into using the [`pathlib`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L98) and [`os`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L105) Python modules, as well as get hands-on learning with the basics of Python's [iterations](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L75), [variable scoping](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L12), and string-manipulation tools like [`rpartition`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L133)!

### 2. The functionality is designed specifically for [renaming audio sample files](https://github.com/isalevine/file-renamer/blob/master/file-renamer-demo.gif) for music producers.
This is a small project as part of my passion for music production. I created this specifically to help rename large numbers of long, repetitive drum sample filenames. 

I use it regularly to format filenames to display properly on my MPC 2500!

### 3. Command-line controls mimic Unix console commands!
[`ls`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L36), [`cd`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L93), and [`pwd`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L32) are all used as commands to navigate the filesystem.

The primary renaming functionality is [`rn`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L45) and [`rn all`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L51).

There's also a WIP help menu that will be accessible via [`h` or `help`](https://github.com/isalevine/file-renamer/blob/c361c8ad9fa424dbda5554f6adb78d134261c16f/script.py#L41)!


## Requirements
* Python3 version 3.7.5 or higher


## Setup
1. Clone this repo.
1. [Update the default directory.](https://github.com/isalevine/file-renamer/blob/0e9e2783b0e967433e40820c6fbe7f7d7759c571/script.py#L7) This is where the CLI will start in your filesystem. I recommend setting it to a common audio sample directory.
1. Open by running `python3 script.py` in the main directory.


## Use
Open by running `python3 script.py` in the main directory.

Use `cd` commands to navigate to the files you want to rename. File Renamer can target individual files, or can do (currently) basic string matching to change multiple filenames in the same directory.

**Example:**

```
INPUT:
Yamaha_DTX-MULTI Kick 01.wav
Yamaha_DTX-MULTI Kick 02.wav
Yamaha_DTX-MULTI Kick 03.wav
Yamaha_DTX-MULTI Snare 01.wav
```
```
$ rn all Yamaha_DTX-MULTI Dtx
```
```
OUTPUT:
Dtx Kick 01.wav
Dtx Kick 02.wav
Dtx Kick 03.wav
Dtx Snare 01.wav
```

Final confirmation (Y/n) will be requested for all multi-file rename commands.

**NOTE: Spaces are not currently handled. Instead, make 1-by-1 changes to individual space-separated words.**

## Commands
**Change Directory:**
```
cd
```

**List Files:**
```
ls
```

**Print Directory:**
```
pwd
```

**Rename (single file, change entire filename):**
```
rn <current_filename.ext> <new_filename.ext>

$ rn Airhorn.wav AIRHOOOORN.wav
```

**Rename All (multiple files, replace LAST string match found in each filename):**
```
rn all <string_input> <string_output>

$ rn all Hihat HH
```

*Note: Currently, using backslashes `\` to represent spaces in filenames is NOT working!*

*Note: Currently, `rn all` will replace ALL matching instances of `<string_input>` encountered in the filename, NOT just the first match encountered.*

**Exit Program:**
```
q / quit
```

<!-- **Help Menu:**
```
h / help
``` -->

## Notes
**Upcoming plans:**
* UNIT TESTS!! Need to find a way to create a dummy file to rename--refer to this StackOverflow article: [https://stackoverflow.com/questions/56760486/unit-testing-of-renaming-files-in-python](https://stackoverflow.com/questions/56760486/unit-testing-of-renaming-files-in-python) / [also, see this StackOverflow about mocking filesystems in Python](https://stackoverflow.com/questions/19672138/how-do-i-mock-the-filesystem-in-python-unit-tests)
* CREATE LOGS!! Find a way to refactor the output of console-printed filename changes (store/update log once, then print the log)
* Add in a way to target single or multiple matches in filename *(i.e. only first "Snare" in "Snare 808 Filter Snare.wav")*
* More complex handling of spaces, underscores, empty strings, special characters, etc.


## Credits
Special thanks to [https://samplesfrommars.com/](https://samplesfrommars.com/) for the incredible samples in use on my MPC. <3