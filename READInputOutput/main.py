# f = open("test_file.txt", "w")  # w - write, r - read, a - append
# f.write("this is going ot be our another line in the file\n")  # \n - new line
# f.write("this is going ot be our another one line in the file\n")  # \n - new line
# f.close()

# f = open("test_file.txt", "r")  # w - write, r - read, a - append
# file_line = f.readline()  # read one line
# print(file_line)  # print one line
# file_line = f.readline()  # read one line
# print(file_line)  # print one line
# file_line = f.readline()  # read one line
# print(file_line)  # print one line
# f.seek(0)  # go to the beginning of the file
# file_line = f.readline()  # read one line
# print(file_line)  # print one line
# f.close()  # close the file


# f = open("test_file.txt", "r")  # w - write, r - read, a - append
# for line in f.readlines():
#     if "4" in line: # read one line
#         print(line)  # print one line
# f.close()  # close the file

# with is a context manager that closes the file automatically
with open("test_file.txt", "r") as f:  # w - write, r - read, a - append
    for line in f.readlines(): # read all lines
        if "4" in line: # read one line
            print(line)  # print one line



