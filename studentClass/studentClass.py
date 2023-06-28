class Student:
    def __init__(self, name, place, age):
        self.name = name
        self.place = place
        self.age = age
        
    def set_age(self, age):
        self.age = age
        
    def get_age(self):
        return self.age
    
    def display_student_details(self):
        print(f"Name: {self.name}, Place: {self.place}, Age: {self.age}")