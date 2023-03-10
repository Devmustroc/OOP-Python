class SumPair:
    def __init__(self, list):
        self.list = list
        self.length = len(list)
        self.i1 = 0
        self.i2 = 1
    def __iter__(self):
        return self

   def __next__(self):

l = SumPair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
