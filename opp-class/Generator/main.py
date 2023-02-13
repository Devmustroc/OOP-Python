import os

def populate_file(filename): # def populate_file(filename):
    value_to_write = ['hello', 'world', 'this', 'is', 'a', 'test'] # value_to_write = ['hello', 'world', 'this', 'is', 'a', 'test']
    with open(filename, 'w') as f: # with open(filename, 'w') as f:
        for value_to_write in value_to_write:   # for value_to_write in value_to_write:
            f.write(value_to_write) # f.write(value_to_write)
            f.write("\n") # new line

def read_is_exist(filename): # def read_is_exist(filename):
    if os.path.isfile(filename):
        yield from read_file(filename)
    return []


def read_file(filename): # def read_file(filename):
    data = []
    with open(filename, 'r') as f:  # with open(filename, 'r') as f:
        for line in f.readlines():  # for line in f.readlines():
            yield line # yield line
            # # return data

    # # return data


filename = "sample.txt"  # filename = "sample.txt"
populate_file(filename)  # populate_file(filename)

# file_content = read_file(filename) # file_content = read_file(filename)

file_content = read_file(filename)  # file_content = read_file(filename)

print(file_content)  # print(file_content)

 #for line in file_content:  # for line in file_content:
    #print(line)  # print(line)

#line = next(file_content)  # line = next(file_content)
#print(line)  # print(line)
#another_line = next(file_content)  # another_line = next(file_content)
#print(another_line)  # print(another_line)