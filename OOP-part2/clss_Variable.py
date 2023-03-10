# class Python:
#     name = 'python'
#     _age = 30
#     __key = '1234'
#
#     def __init__(self):
#         pass
#
#     def python_code(self):
#         print("I am a python developper!")
#
#
# py = Python()
# py.python_code()
# py.__init__()


class Coder():
    def __init__(self, name):
        self.Name = name

    def get_lang(self, lang):
        self.language = lang

    def display_lang(self):
        lang_str = ", ".join(self.language)
        print(f"I am a {lang_str} developer!")

    def is_Pythoner(self):
        if "python" in self.language:
            print("Yes, I am a Python developer!")
        else:
            print("No, I am not a Python developer!")

cd = Coder("jake")
cd.language = ["python", "java", "c++"]
cd.display_lang()
cd.is_Pythoner()
