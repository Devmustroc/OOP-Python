class SumPair:
    def __init__(self, list):
        self.list = list
        self.length = len(list)
        self.i1 = 0
        self.i2 = 1
    def __iter__(self):  # this is a must for iterable class
        return self

    def __next__(self):  # is for iterator class
        if self.i2 == self.length: # if the index is out of range
            raise StopIteration # raise the StopIteration exception
        else: # if the index is in range
            self.i1 += 1  # increment the index
            self.i2 += 1  # increment the index
            return self.list[self.i1-1] + self.list[self.i2-1] # return the value at the index


l = SumPair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
m = SumPair([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
for ele in m:
    print(ele)
