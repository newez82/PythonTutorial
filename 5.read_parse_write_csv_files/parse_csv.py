"""
    csv modules for read and write
"""
import csv

with open("5.read_parse_write_csv_files\\names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    print("Print out the content of the csv file using for loop:")
    for line in csv_reader:
        print(line)

# use index to print out the email only
with open("5.read_parse_write_csv_files\\names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    print("\nPrint out the value from index 2:")
    for line in csv_reader:
        print(line[2])

with open("5.read_parse_write_csv_files\\names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    print("\nSkip the first line by using next() function:")
    next(csv_reader)
    for line in csv_reader:
        print(line[2])

# Save the content into a new file with dash delimiter
with open("5.read_parse_write_csv_files\\names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    with open(
        "5.read_parse_write_csv_files\\new_names.csv", "w", newline="", encoding="UTF-8"
    ) as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")
        for line in csv_reader:
            csv_writer.writerow(line)


# dictionary reader and writer, it easier to print out email using email key instead of index
with open("5.read_parse_write_csv_files\\names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print(
        "\nPrint out the content of the csv file using for loop with dictionary reader:"
    )
    for line in csv_reader:
        print(line)

with open("5.read_parse_write_csv_files\\names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print("\nPrint out the email by passing the key:")
    for line in csv_reader:
        print(line["email"])

# Save the content into a new file using dictionary wrtier
with open("5.read_parse_write_csv_files\\names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open(
        "5.read_parse_write_csv_files\\new_names.csv", "w", newline="", encoding="UTF-8"
    ) as new_file:
        fieldnames = ["first_name", "last_name"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
        csv_writer.writeheader()

        for line in csv_reader:
            # do not write email field into the new file
            del line["email"]
            csv_writer.writerow(line)
