"""
    File Objects
"""
# Open a file, default to opening the file for reading if not specific which operation to pass in
# r - read
# w - write
# a - append
# r+ - read/write
FILE_PATH_READ = (
    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\file_objects\\test.txt"
)
FILE_PATH_WRITE = (
    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\file_objects\\test_write.txt"
)

FILE_PATH_COPY = (
    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\file_objects\\test_copy.txt"
)

FILE_PATH_JPG = (
    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\file_objects\\shiba.jpg"
)

FILE_PATH_JPG_COPY = (
    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\file_objects\\shiba_copy.jpg"
)

FILE_MODE_READ = "r"
FILE_MODE_WRITE = "w"
FILE_MODE_READ_BINARY = "rb"
FILE_MODE_WRITE_BINARY = "wb"
FILE_ENCODING_UTF8 = "utf-8"
FILE_ENCODING_BYTES = "utf-8"
f = open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
)
print("Name of the file:", f.name)
print("current mode of the file:", f.mode)
# close the file after reading it.
f.close()

print("\n\nCheck the file has closed:", f.closed)

# Open file using content manager without explicit close the file,
# and previous method will end up with leaks that cause to run over max.
# which allowed file descriptor on the system and application will throw
# the error.

with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as f:
    # Use f.read() for small file to load it to memory or read certain characters at a time
    f_contents = f.read()
    print("Print the content of the file using read() method:\n", f_contents, "\n")

with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as f:
    # read certain characters at a time
    SIZE_TO_READ = 10
    f_contents = f.read(SIZE_TO_READ)
    print(
        "read certain characters at a time by passing number into parameter:\n",
        f_contents,
        "\n",
    )

with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as f:
    # use f.readlines() to print out each line in a list
    f_content_lines = f.readlines()
    print(
        "Print the content of the file using readlines() method:\n",
        f_content_lines,
        "\n",
    )

    # use f.readline() to print out each line in a list, everytime when we run readline(),
    # it gets the next line in our file
    # pass in end='' in the second parameter, it will not adding the new line
with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as f:
    f_content_line = f.readline()
    print(
        "Print the first line of the file using readline() method:\n",
        f_content_line,
        end="",
    )

print("\nprint the content of the file using for loop:")
with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as f:
    # read entire content from a large file using for loop
    for line in f:
        print(line, end="")


print("\n\nprint the content of the file using while loop:")
with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as f:
    # read entire content from a large file using while loop
    f_contents = f.read(SIZE_TO_READ)
    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f.read(SIZE_TO_READ)


with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as f:
    f_contents = f.read(SIZE_TO_READ)
    # Use f.tell method to tell us the current position in the file
    print("\n\nCurrent position in the file:", f.tell())
    print(f_contents, end="*")

    # Use f.seek method to set the position in the file
    print("\n\nCurrent position in the file:", f.seek(4))
    f_contents = f.read(SIZE_TO_READ)
    print(f_contents, end="*")


# Write to a file, open with write mode will create a file if the file doesn't exists.
# It will override the current file if file exists
with open(
    FILE_PATH_WRITE,
    FILE_MODE_WRITE,
    encoding=FILE_ENCODING_UTF8,
) as f:
    f.write("Test")
    # file seek won't override anything, only override
    # from the position to the end of the word or sentence.
    f.seek(0)
    # When do another write, it will pick up where we left off
    f.write("R")


# Copy the file
with open(
    FILE_PATH_READ,
    FILE_MODE_READ,
    encoding=FILE_ENCODING_UTF8,
) as readfile:
    with open(
        FILE_PATH_COPY,
        FILE_MODE_WRITE,
        encoding=FILE_ENCODING_UTF8,
    ) as writefile:
        for line in readfile:
            writefile.write(line)

# Copy picture file using binary mode to read byte instead of UTF8
# by using rb (read binary) and wb (write binary) in the file mode
with open(FILE_PATH_JPG, FILE_MODE_READ_BINARY) as readfile:
    with open(
        FILE_PATH_JPG_COPY,
        FILE_MODE_WRITE_BINARY,
    ) as writefile:
        for line in readfile:
            writefile.write(line)
