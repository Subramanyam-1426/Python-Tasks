class studentmanagement:
    # Defines the maximum number of subjects allowed.
    MAX_SUBJECTS = 5
    # Defines the minimum passing mark.
    PASS_MARK = 35
    # Stores the total number of students.
    total_students = 0
    # Stores the college name shared by all students.
    cname = "Aditya Institute of Technology"
    # Initializes a new student with roll number, name, and branch.
    def __init__(self, roll_no, name, branch):
        self._roll_no = roll_no
        self.name = name
        self._branch = branch
        self.__marks = {}
        # self.average=0.0
        studentmanagement.total_students += 1

    # Calculates and returns the student's average marks.
    @property
    def average(self):
        dmmarks = self.__marks
        sum = 0
        n = len(dmmarks)
        for k, v in dmmarks.items():
            sum += v
        return sum / n

    # Returns the grade based on the student's average marks.
    @property
    def grade(self):
        check = self.average
        if check >= 90:
            return "A+"
        elif check >= 75 and check <= 89.99:
            return "A"
        elif check >= 60 and check <= 74.99:
            return "B"
        elif check >= 35 and check <= 74.99:
            return "C"
        else:
            return "F"

    # Returns the student's roll number.
    @property
    def roll_no(self):
        return self._roll_no

    # Adds and validates marks for the given subjects.
    def add_marks(self, subject, **mark):
        if subject > studentmanagement.MAX_SUBJECTS:
            raise ValueError(f"Subject are more than {studentmanagement.MAX_SUBJECTS}")
        for k, v in mark.items():
            if (not isinstance(v, (int, float))):
                raise TypeError("the marks are must be in integer type")
            if v < 0 or v > 100:
                raise ValueError(f"the marks must be b/w 0 and 100")
            self.__marks[k] = v

    # Returns a copy of the student's marks.
    def get_marks(self):
        dmmarks = dict((self.__marks))
        return dmmarks

    # Checks whether the student has passed all subjects.
    def has_passed(self):
        dmmarks = self.get_marks()
        for k, v in dmmarks.items():
            if v < 35:
                return False
        return True

    # Changes the student's branch.
    def change_branch(self, new_branch):
        old = self._branch
        self._branch = new_branch
        return f"Student {self.name} changed Branch from {old} to {self._branch}"

    # Returns the total number of students.
    @classmethod
    def get_total_students(cls):
        return cls.total_students

    # Checks whether the given mark is valid.
    @staticmethod
    def is_valid_mark(mark):
        if (not isinstance(mark, (int, float))):
            raise TypeError(f"the enter marks must be the integer type")
        if mark > 100 or mark < 0:
            return False
        return True

    # Returns a readable string containing the student's details.
    def prints(self):
        return (f"Student [{self.roll_no}] {self.name} | {self._branch} | Avg: {self.average} | Grade : {self.grade}")


# Demonstrates student creation and various student management operations.
def main():
    try:
        print(f"College : {studentmanagement.cname}")

        s1 = studentmanagement(101, "Aravind", "CSE")
        s2 = studentmanagement(102, "Subramanyam", "CSE")

        print(f"Total : {studentmanagement.total_students}")

        s1.add_marks(3, Maths=92, Physics=88, Chemistry=76)
        s2.add_marks(3, Maths=98, Physics=33, Chemistry=79)

        print(f"s1 marks: {s1.prints()}")
        print(f"s2 marks: {s2.prints()}")

        print(s1.get_marks())
        print(f"s1 passed : {s1.has_passed()}")
        print(f"s2 passed : {s2.has_passed()}")

        print(s1.change_branch("IT"))
        print(f"is_valid_mark(105) : {studentmanagement.is_valid_mark(105)}")

    except (TypeError, ValueError) as err:
        print(err)

    try:
        s3 = studentmanagement(477, "Varun", "CSE")
        s3.add_marks(3, Maths=150, Physics=88, Chemistry=76)
    except (TypeError, ValueError) as err:
        print(err)

    try:
        s4 = studentmanagement(121, "Bhargav", "CSE")
        s4.add_marks(3, Maths=99, Physics=88, Chemistry=76)
        s4.average = 56
    except (TypeError, ValueError, AttributeError) as err:
        print(f"Blocked : {err}")

    try:
        s5 = studentmanagement(463, "vivek", "CSE")
        s5.add_marks(3, Maths=94, Physics=68, Chemistry=54)
        s5.roll_no = 456
    except (TypeError, ValueError, AttributeError) as err:
        print(f"Blocked : {err}")

    print("protected : ", s1._branch)

    samp = s1.get_marks()
    samp["Maths"] = 30
    print("protected : ", s1.get_marks())


# Executes the program when this file is run directly.
if __name__ == "__main__":
    main()