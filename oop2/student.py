from abc import ABC, abstractmethod


# Abstract class
class Student(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_dept(self):
        pass

    @abstractmethod
    def set_dept(self, dept):
        pass
