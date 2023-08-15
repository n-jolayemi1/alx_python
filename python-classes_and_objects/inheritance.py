""" 
This code is to test for python inheritance
"""

class university:

    def __init__(self, department=None, lecturers=None):
        self.department = department
        self.lecturers = lecturers

    @property
    def department(self):
        return self.__department
    
    @department.setter
    def department(self, department):
        self.__department = department

    @property
    def lecturers(self):
        return self.__lecturers
    
    @lecturers.setter
    def lecturers(self, lecturers):
        self.__lecturers = lecturers

    def uni_def(self):
        return "I am University that has {} lecturers with {} departments".format(self.__lecturers, self.__department)
    


university = university(10, 20)
unidef = university.uni_def()
print(unidef)