## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os


def find_files(suffix = "", path = "."):
    file_list = []
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
    else:
        newpath = os.listdir(path)

        for filename in newpath:
            file_list += find_files(suffix, "{}/{}".format(path, filename))
    return file_list

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))

""" TEST CASE - 1"""
print(find_files('.h','.'))
# Expected output: Prints all filenames with the extension having .h

""" TEST CASE - 2"""
print(find_files('', ''))
#Expected output: Prints all the files in the path provided

""" TEST CASE - 3"""
print(find_files('.h', '.'))
# Expected output: As we have not specified the path the default path will be the current directory.

print(find_files('12345','.'))