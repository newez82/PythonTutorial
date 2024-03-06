""" Before python runs any code, it sets a few speical variables.
    __name__ is one of the special variables. it sets __name__ equal to __main__.
    when we import a module, it's going to set __name__ variable to the file of the file.
"""


def main():
    """main method"""
    print(f"Run directly - first module's name: {__name__}")


# it checks is the file being run directly by Python
# or is it beging imported
if __name__ == "__main__":
    main()
else:
    print("Run from Import")
