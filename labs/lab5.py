class Student():
    school = '123'
    
    @classmethod
    def get_school(cls):
        return cls.school

    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade
    
    def __str__(self):
        return f'\nname = {self.name} \nage = {self.age} \ngrade = {self.grade}'
    
    @property
    def name(self):
        """returns _name of the student"""
        return self._name
    
    @property
    def age(self):
        """returns _age of the student"""
        return self._age
    
    @property
    def grade(self):
        """returns _grade of the student"""
        return self._grade
    
    @age.setter
    def age(self, value):
        """Sets the age of the Student. Must be positive"""
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be positive")
        

    def get_info(self):
        return f'\nStudent info:\nname = {self.name} \nage = {self.age} \ngrade = {self.grade}'
    
    def promote(self):
        self._grade = self._grade + 1
    
sergei = Student('sergei', 16, 11)
anna = Student('Anna', 15, 9)
print(sergei)
print(sergei.get_info())
sergei.promote()
sergei.age = 15
print(sergei.get_info())

print(anna)
print(anna.get_info())
anna.promote()
print(anna.get_info())


