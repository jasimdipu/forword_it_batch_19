from student import Student


class StudentImpl(Student):

    # encapsulation -> 1. private __, 2. protected _ , 3. public

    def __init__(self, name, dept, sem):
        self.__name = name
        self.__dept = dept
        self._sem = sem

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dept(self):
        return self.__dept

    def set_dept(self, dept):
        self.__dept = dept

    def __str__(self):
        return "Name: " + self.__name + "\nDept: " + self.__dept


class Examples(StudentImpl):
    def __init__(self, name, dept, sem, test=0):
        StudentImpl.__init__(self, name, dept, sem)
        self.test = test

    def get_sem(self):
        return self._sem

    def get_aname(self):
        return self.__name


# student = StudentImpl("Tamim", "CSE", "5th")
# print(student)
# # print(student.name)
# # print(student.dept)
# # print(student.sem)
# print(student.get_name())
# print(student.get_dept())
#
# ex = Examples("Tamim", "CSE", "5th")
# print(ex.get_sem())
# # print(ex.get_aname())
