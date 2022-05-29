# Worldle Solver
This can solve Wordle problems, ideally with some green, orange, or excluded
letters.

## USAGE:
Either run `python3 wordle.py` and follow the input instructions, or run `python3 wordle.py file_name.txt`to read the information from a file.

To input a green letter use uppercase, and for orange letters use lowercase. When using either file or command-line input, enter a blank line if no letters are known for that column. If no letters are excluded, then the line for all available letters can be left blank.

The file should be of format:

    First Column Letters
    Second Column Letters
    Third Column Letters
    Fourth Column Letters
    Fifth Column Letters
    All Available Letters 
