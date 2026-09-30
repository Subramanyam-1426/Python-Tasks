# Im going to demonstrate the basic Builder design pattern version that is helpful for object validation
# before it's actually going to create a one

class Builder:
    def __init__(self):
        self._name = ""
        self._age = 0
        self._rollno = ""
        self._branch = ""
        self._grad_year = 0

    def set_name(self, name): self._name = name

    def set_age(self, age):  self._age = age

    def set_rollno(self, rollno): self._rollno = rollno

    def set_branch(self, branch): self._branch = branch

    def set_grad_year(self, grad_year): self._grad_year = grad_year

    @property
    def name(self): return self._name

    @property
    def age(self): return self._age

    @property
    def roll_no(self): return self._rollno

    @property
    def branch(self): return self._branch

    @property
    def grad_year(self): return self._grad_year


class Student:
    def __init__(self, builder):
        if builder.grad_year > 2026:
            raise ValueError("Grad year cannot be greater than 2026")
        self.name = builder.name
        self.age = builder.age
        self.grad_year = builder.grad_year
        self.roll_no = builder.roll_no
        self.branch = builder.branch


builder = Builder()
builder.set_age(21)
builder.set_name("Naman")
builder.set_grad_year(2027)     # will trigger the validation error

st = Student(builder)
print(st.age)
print(st.name)
print(st.grad_year)

#ques 1:  How would anyone using your student class know that there is a builder class and realize that they 
# have to create a builder object first and pass that builder to student??

# ques 2: In new Student(builder), who validates and creates? Student's constructor. Builder just
#  holds values. A class called Builder that doesn't build anything is backwards. Give it a build().

