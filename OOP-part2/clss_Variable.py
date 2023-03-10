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


# class Coder():
#     def __init__(self, name):
#         self.Name = name
#
#     def get_lang(self, lang):
#         self.language = lang
#
#     def display_lang(self):
#         lang_str = ", ".join(self.language)
#         print(f"I am a {lang_str} developer!")
#
#     def is_Pythoner(self):
#         if "python" in self.language:
#             print("Yes, I am a Python developer!")
#         else:
#             print("No, I am not a Python developer!")
#
# cd = Coder("jake")
# cd.language = ["python", "java", "c++"]
# cd.display_lang()
# cd.is_Pythoner()

# class Algerba():
#     def __init__(self, r=0.0,i=0.0):
#         self.real = r
#         self.imag = i
#
#     def __add__(self, other):  # overload the + operator other is another Algerba object
#         self.real += other.real
#         self.imag += other.imag
#         return self
#
#     def show_Value(self):
#         print(self.real, self.imag)
#
#
# num = Algerba(3.0, -4.5)
# num1 = Algerba(2.0, 3.5)
# num3 = num1 + num
# num3.show_Value()

class Numeric_String:
    def __init__(self, Str = ''):
        self.Str = Str

    def __int__(self):
        return int(self.Str)

num = Numeric_String('1024')
pro = int(num.Str) * 2
print(pro)