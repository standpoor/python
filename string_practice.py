# please google "pyformat" to check the details.
a = 3.1415926
b = 13
c = 9

string = "here is the result:{0:.3f}{1:3d}{2:3d}".format(a, b, c)
print(string)

number = 12345678
print(f"{number:,}")

number2 = 123.1415926
print(f"{number2:.2f}")

number3 = 127
print(f"{number3:x}")

number3 = '1234'
print(f"{number3:>5}")  # keep 5 character space and aligne with the right side

number3 = '1234'
print(f"{number3:_>5}")

number3 = '1234'
print(f"{number3:^6}") # 6 character space and keep the string in the middle

text = "abc" + "def" # string concatenate
print(f"{text}")

text = "abc_def"
text_splited = text.split("_")
print(text_splited)
print("*".join(text_splited))

search_text = "allen is I"
if search_text.capitalize().startswith("Allen"):
    print("I am Allen")
else:
    print("I am not Allen")