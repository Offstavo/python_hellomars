class Person():
    def __init__(self, age, name):#self refers to the object itself
        self.f_name = name
        self.my_age = age

person_one = Person(15,"John")   
person_two = Person(25,"Mary")
person_three = Person(30,"Kate") 

print(f"The first person is called {person_one.f_name} and is aged {person_one.my_age}")
print(f"The first person is called {person_two.f_name} and is aged {person_one.my_age}")
print(f"The first person is called {person_three.f_name} and is aged {person_one.my_age}")