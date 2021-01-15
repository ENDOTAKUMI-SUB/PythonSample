class MyClass1:
    def __init__(self, text="abc"):
        self.text = text

a = MyClass1()
b = MyClass1(text="ggg")
c = MyClass1(text="uds")

print(a.text)
print(b.text)
print(c.text)