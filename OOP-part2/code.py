class Code:
    def __init__(self, name):
        self.Name = name

    def info(self):
        print("Name: ", self.Name)

    def is_JS(self):
        if "python" in self.language:
            print("Yes, I am a JS developper!")
        else :
            print("No, I am not a JS developper!")


cd = Code("jake")
cd.language = ["python", "java", "c++"]
cd.info()
cd.is_JS()

