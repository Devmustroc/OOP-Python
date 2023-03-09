class Code:
    def __init__(self, name):
        self.Name = name

    def info(self):
        print("Name: ", self.Name)

    def is_Pythoner(self):
        if "python" in self.language:
            print("Yes, I am a Pythoner!")
        else :
            print("No, I am not a Pythoner!")


cd = Code("jake")
cd.language = ["c++", "c#"]
cd.is_Pythoner()
del cd.language
print(cd.language)

