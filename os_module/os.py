"""
    underlying operating system functionality
        - navigate the file system
        - get file information
        - lookup and change the enviornment variable
        - move file around
"""
import os
from datetime import datetime

print(
    "dir(os) shows us all the attributes and methods that we have access to:\n",
    dir(os),
    "\n",
)

print("Get Current Directory: ", os.getcwd(), "\n")

# Change directory
os.chdir("c:\\Users\\chin.p.ho\\Documents\\")
print("Get Changed Directory: ", os.getcwd(), "\n")


print(
    "List of the files and folders in current directory without passing any path in the parameter:\n",
    os.listdir(),
    "\n",
)

# Create new folder on desktop named as OS-Demo-2 with the following options
# os.mkdir('OS-Demo-2')
# os.mkdirs('OS-Demo-2/Sub-Dir-1')
#   it will create the folder thats a few levels deep, it will create all the
#   intermediate level directories

# Delete folder
# os.rmdir('OS-Demo-2')
# os.removedirs('OS-Demo-2/Sub-Dir-1')
# It will remove the intermediate directories

# Rename file or folder
# os.rename('test.txt', 'demo.txt')
#   pass in the original file name in first parameter and new file name in second parameter

# print out metadata of the file
print("print out all the information about the file: \n", os.stat("desktop.ini"), "\n")
print(
    "print out the size in byte for the file by using st_size attribute:",
    os.stat("desktop.ini").st_size,
    "bytes.",
    "\n",
)

# convert the timestamp into human readable format using datetime.fromtimestamp() method
print(
    "print out the last modified time of the file by using st_mtime attribute:",
    datetime.fromtimestamp(os.stat("desktop.ini").st_mtime),
    "\n",
)


# print out all directory in a file by using os.walk() method.
# it is a 3 values tuples which includes dirpath, dirname, filenames
# for dirpath, dirname, filenames in os.walk(
#    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\"
# ):
#    print("current path: \n", dirpath)
#    print("directories: \n", dirname)
#    print("files: \n", filenames)


# get environment variable by using os.environ
print("Get the value of current PATH enviornment: ", os.environ.get("PATH"), "\n")

# Create a new file and concat the location of directory with the new file by using os.path().join()
print(
    "Concat the directory with a file:",
    os.path.join("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\", "test.txt"),
)

# get the filename of any path that we are working on using os.path.basename()
print(
    "Grab the filename from the path:",
    os.path.basename("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\test.txt"),
)

# get the directory name of any path that we are working on using os.path.dirname()
print(
    "Grab the directory name from the path:",
    os.path.dirname("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\test.txt"),
)

# get the directory and file name of any path that we are working on using os.path.split()
print(
    "Grab the directory and file name from the path:",
    os.path.split("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\test.txt"),
)

# check path exists
print(
    "Check the path exists:",
    os.path.exists("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\test.txt"),
)

# Check the name without extension is directory
print(
    "Check the name without extension is directory:",
    os.path.isdir("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\test"),
)

# Check the name without extension is file
print(
    "Check the name without extension is file:",
    os.path.isfile("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\test"),
)

# split file and extension
print(
    "Split file and extension:",
    os.path.splitext("c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\test.txt"),
)
