class Student :
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount):
        self.height += amount

    def study(self):
        print(f"{self.name} is busy studying")

my_student = Student ("Bob", 120)
my_student.grow(int(input("how much does the student grow by: ")))
print(my_student.name, my_student.height)
my_student.study()