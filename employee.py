"""
Define the Employee class with an __init__() method
Define a class variable new_id and set it equal to 1
Each Employee instance will need its own unique ID. Thus, inside __init__(), define self.id and set it equal to the class variable new_id
Lastly, increment new_id by 1
Define a say_id() method
Inside say_id(), output the string "My id is " and then the instance id.
Define the variable e1 and set it to an instance of Employee
Define the variable e2 and set it to an instance of Employee
Have both e1 and e2 output their ids
"""
class Employee:
        new_id=1
        def __init__(self):
                self.name=input("enter name:")
                Employee.new_id+=1
                self.id=self.new_id
        def say_id(self):
                return (f"{self.name}'s id is {self.id}")

e1=Employee()
e2=Employee()
print(e1.say_id())
print(e2.say_id())
                