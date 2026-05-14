"""
    Lesson: Working with csv file
    Date: Wed May 13 2026
"""

# What is CSV ?
# CSV stand for Comma Seperated Values.


# Read CSV file with Reader Metho


# # first import the csv
# import csv

# import csv
# data = []
# # using file handling to open the csv file
# with open("csvfiles/demo.csv", "r") as rcsv:
#     # allow to read and return the iterator object
#     # initial space removing and remove the QUOTING
#     csv_reader = csv.reader(rcsv, skipinitialspace=True, quoting=csv.QUOTE_ALL)
#     # Extracting field  names through first row - next() function returns the next items from the iterator
#     field = next(csv_reader)
#     print(field)
#     # new will iterator with second line because I have already do with next() first line
#     dict_data = {}
#     for line in csv_reader:
#         for key, value in zip(field, line):
#             dict_data[key] = value
#         data.append(dict_data)


# # Alternative
# data1 = []
# with open("csvfiles/demo.csv", "r") as rcsv:
#     csv_reader = csv.DictReader(
#         rcsv, skipinitialspace=True, quoting=csv.QUOTE_ALL)

#     for rows in csv_reader:
#         data1.append(rows)

# print(data1)


# # read a csv file and print only 5 rows
# rows = []
# with open("csvfiles/demo.csv", "r") as rcsv:
#     csv_reader = csv.reader(rcsv, skipinitialspace=True, quoting=csv.QUOTE_ALL)
#     field = next(csv_reader)
#     print(field)

# #   Iterating the csv_reader rows
#     for row in csv_reader:
#         rows.append(row)

# print(len(rows))  # has 59 records

# # only printing the  5 rows with name of the flim and genre
# for row in rows[5:10]:
#     print(f"Name of flim: {row[0]} and Genre: {row[1]}")


# write a CSV file after read from another

# Manual work done by myself
import json
import csv

try:
    with open("csvfiles/demo.csv", "r") as rcsv:
        csv_reader = csv.reader(
            rcsv, skipinitialspace=True, quoting=csv.QUOTE_ALL)

        with open("csvfiles/write.csv", "w") as f:
            for line in csv_reader:
                each_line = ""
                for l in line:
                    each_line += l + ","
                each_line = each_line[0:len(each_line) - 1]
                f.write(each_line + "\n")
except FileNotFoundError:
    print("File not found error")
finally:
    print("Done work")


# better way or using functions
import csv
with open("csvfiles/demo.csv", "r") as rcsv:
    csv_reader = csv.reader(rcsv, skipinitialspace=True, quoting=csv.QUOTE_ALL)
    fields = next(csv_reader)
    with open("csvfiles/write.csv", "w") as wcsv:
        # it is already store in fields because use next() iterator it will not iterate this now
        csv_writer = csv.writer(wcsv)
        csv_writer.writerow(fields)  # saving the field firstly saftey
        # csv_writer.writerows(csv_reader)  # after writing the rows of that readed by csv.reader

        # also can use loop it is more controlled because for example I want to write only the first 5 records
        """ count = 1
         for line in csv_reader:
             if count > 5:
                 break
             csv_writer.writerow(line)
             count += 1
        """

# Write a csv file with tab delimited and rows between 5 to 10

import csv
# rows = []
with open("csvfiles/demo.csv", "r") as rcsv:
    csv_reader = csv.reader(rcsv, skipinitialspace=True,
                            quoting=csv.QUOTE_ALL)
    field = next(csv_reader)
    with open("csvfiles/write2.csv", "w") as wcsv:
        csv_writer = csv.writer(wcsv, delimiter="\t")
        csv_writer.writerow(field)
        # It is my way but I can do better
        """
        for row in csv_reader:
            rows.append(row)
        
        for row in rows[5:11]:
            csv_writer.writerow(row)
        """

        # My way is doing by coverting the csv_reader object into directly in list and write from slice 5 to 10
        for row in list(csv_reader)[5:11]:
            csv_writer.writerow(row)


# read csv file with dictonary method

# Doing it manually
import csv
dict_list = []
with open("csvfiles/demo.csv", "r") as rcsv:
    csv_reader = csv.reader(rcsv, skipinitialspace=True, quoting=csv.QUOTE_ALL)
    fields = next(csv_reader)
    for row in csv_reader:
        dict_value = {}
        for key, value in zip(fields, row):
            dict_value[key] = value
        dict_list.append(dict_value)

print(dict_list)

# Doing using the built-it function called DictReader and write in other file as a dict value

# writing the dict file into csv file
dict_list = []
with open("csvfiles/demo.csv", "r") as rcsv:
    csv_dict_reader = csv.DictReader(
        rcsv, skipinitialspace=True)
    fields = next(csv_dict_reader)
    for row in csv_dict_reader:
        dict_list.append(row)

with open("csvfiles/demodict.csv", "w") as wdcsv:
    csv_dict_writer = csv.DictWriter(wdcsv, fieldnames=fields)

    # Write header for get the field first
    csv_dict_writer.writeheader()

    # csv_dict_writer.writerows()

    # It is more control rather then using whole
    for row in dict_list[5:11]:
        csv_dict_writer.writerow(row)


# Challenge
mydict = [
    {'Name': 'Prosenjit', 'Age': '40', 'Computer-Language': 'Java'},
    {'Name': 'Atreyee', 'Age': '15', 'Computer-Language': 'Java'},
    {'Name': 'Artrika', 'Age': '11', 'Computer-Language': 'Python'}
]
"""
    with open("csvfiles/demodict.csv", "w") as wcsv:
    fields = ",".join(mydict[0].keys())
    wcsv.write(fields + "\n")
    for line in mydict:
        wcsv.write(",".join(line.values()) + "\n")
"""

with open("csvfiles/demodict.csv", "w", newline="") as wcsv:
    writer = csv.DictWriter(wcsv, fieldnames=mydict[0].keys())
    writer.writeheader()
    for row in mydict:
        writer.writerow(row)
