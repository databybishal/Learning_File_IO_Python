
# Character                       Meaning
# 'r'                   open for reading (default)
# 'w'                   open for writing, truncating the file first
# 'x'                   create a new file and open it for writing
# 'a'                   open for writing, appending to the end of the file if it exists
# 'b'                   binary mode
# 't'                   text mode (default)
# '+'                   open a disk file for updating (reading or writing)


# Lesson: How to read in file

# to open the file, I have open method with path 'demo.txt' and use mode read 'r'
# default the file mode is text I need binary the put other
f = open("demo.txt", "r")
# like ('rb' for binary) t is default
# assign the whole read data in data using the f.read() function
data = f.read()
# assign mean particular set of character like (5) mean file character
print(data)  # printing the whole data
print(type(data))  # printing the type of data
f.close()  # always close after work done


f = open("demo.txt", "r")
# assign number help you to read particular set of data like 5 string
data = f.read(5)
print(data)
f.close()

f = open("demo.txt", "r")
# also read line using the readline() functions
line1 = f.readline()  # always give extra line space \n. It produce that
print(line1)
line2 = f.readline()
print(line2)
f.close()

# always note: If one time data is read, it create problem, because it is actual pointer
# if there no data more in file always return empty nextline


# Lesson: How to write in file

# IF I have to override the file then always use "w" mode
# It will write after trucating the whole data in file
f = open("demowrite.txt", "w")
f.write("I want to learn Javascript tomorrow. 123")
f.close()

# IF I have to add or write the data in file without truncating the whole file then we use append mode 'a'
f = open("demowrite.txt", "a")
f.write("\nI want learn python")  # add the file with nextline
f.write("\nAfter that pyspark")  # add the file with nextline
f.close()

# if the file does not exists in append mode. It automatically I create a file with write mode and append mode
# the file not exists then it will create file same with append too
f = open("simple.txt", "w")
f.write("test")  # it is optional , it will work without any write
f.close()

# with same as append
# the simple1.txt does not exists then it will create new file name simpel1.txt
f = open("simpel1.txt", "a")
f.write("Test")  # It is optional
f.close()

# Combining reading and write
# IF I want to read and write and overwrite from the beginning then we can use "r+"
f = open("democombination.txt", "r+")
f.write("abc")
print(f.read())  # after overwrite point start to print from the where the pointer is
f.close()

# IF I want to truncate the file first and write and after that read the we can use "w+" mode
f = open("demo3.txt", "w+")
# If I do first read there will be noting because first it truncating and wiped down all the data
print(f.read())
f.write("abc")  # after that I write it
f.close()

# If I want to read and write with apppend mode the we can use "a+"
f = open("demo4.txt", 'a+')
print(f.read())  # wil be nothing append make the pointer at the end of the data
f.write(" Koirala")
f.close()


# Better syntax: Demo: no need to close the file at the end, It will close it self
# using read mode
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)


# How to delete file
# use os module which help to delete filename
# have to import the module

# import os # it is pre-built in modules
# os.remove("test.txt")


# Challenge
# Create a new file "practice.txt" using python. Add the following data in it.

# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java

# WAF that replace all occurrence of "java" with "python" in above file.

# Search if the word "learning" exists in the file or not

# First Task
with open("practise/practise.txt", "w") as f:
    f.write(
        "Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java."
    )

# Task


def replace_java(target_word: str, replace_word: str, path: str) -> None:
    with open(path, "r+") as f:
        data = f.read()
        new_data = data.replace(target_word, replace_word)

        f.seek(0)  # move pointer to beginning
        f.write(new_data)  # overwrite file
        f.truncate()  # remove leftover content


replace_java("Java", "Python", "practise/practise.txt")

# Task


def check_for_word(word: str, path: str) -> bool:
    with open(path, "r") as f:
        return word in f.read()


print(check_for_word("learning", "practise/practise.txt"))

# Task


def check_for_line(word: str, path: str) -> int:
    line_no = 1
    with open(path, "r") as f:
        while True:
            data = f.readline()
            if not data:
                break
            if word in data:
                return line_no
            line_no += 1
    return -1


print(check_for_line("jkdjrf", "practise/practise.txt"))

# Task


def count_even_number(path):
    with open(path, "r") as f:
        return sum(1 for i in f.read().split(",") if int(i.strip()) % 2 == 0)



print(count_even_number("practise/practise2.txt"))
