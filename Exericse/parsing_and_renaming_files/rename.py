"""
    renaming files in order
"""
import os

os.chdir("Exericse\\video_files")

for filename in os.listdir():
    file_name, file_ext = os.path.splitext(filename)
    file_title, file_course, file_num = file_name.split("-")
    file_title = file_title.strip()
    file_course = file_course.strip()
    # add padding 0 as prefix using zfill() method
    file_num = file_num.strip()[1:].zfill(2)
    FILE_RENAMED = f"{file_num}-{file_title}{file_ext}"
    print(FILE_RENAMED)
    os.rename(filename, FILE_RENAMED)
