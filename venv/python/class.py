class Computer:
    def func(self,name):
        print("My name is Shivam")
        print("My name is Shivam "+ name)
# creating object of the computer class
v= Computer()
# calling the function
v.func("Tiwari")
Computer.func(v,"shivam")