# File Renamer
A Python CLI for renaming single and multiple files. Designed to format sample filenames for drum machines, but you can use it for whatever kind of files you want! :)

**NOTE: Default directory is currently set to a _.gitignore_-ed folder of drum samples. Make sure to update this in order to avoid errors! _(As of 10-6-2019, see line 37.)_**

![gif of file-renamer in use on the command line](https://thepracticaldev.s3.amazonaws.com/i/a1x2gfq43ukv57cydwqf.gif)


## Use
Open by running ```python3 script.py``` in the main directory.

Use ```cd``` commands to navigate to the files you want to rename. File Renamer can target individual files, or can do (currently) basic string matching to change multiple filenames in the same directory.

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

**Rename All (multiple files, replace all string matches):**
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