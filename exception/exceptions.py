"""
    try/catch exception
"""
try:
    f = open("exception\\test_file.txt", encoding="UTF-8")
    # raise exception if needed
    if f.name == "exception\\test_file.txt":
        raise Exception
except FileNotFoundError as e:
    print("file doesn't exists:", e)
except Exception as e:
    print("General Exception:", e)
# else will execute if try block doesn't raise any exception
# we can move the else code in try block, but it is better
# to leave the try block for something we want to catch
# specially
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
