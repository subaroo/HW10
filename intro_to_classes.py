class Student(object):
    count = 0
    school = "fun school"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.favorite_color = None
        Student.count += 1
        pass

    def talk(self):
        print "I love python!"


bob = Student("Bob", 20)
fred = Student("Fred", 21)
print bob.name
print fred.age
print Student.count
sally = Student("Sally", 22)
print Student.count  # Student count updates to three

fred.favorite_color = "blue"
print fred.favorite_color 
print bob.favorite_color  # We never gave Bob a favorite color

fred.leastfavorite_color = "red"
print fred.leastfavorite_color
# print sally.leastfavorite_color  # We never created this variable for Sally


# This doesn't change Student.school, but creates a member variable for fred
fred.school = "this"
print fred.school
print Student.school  # Still fun school
print sally.school  # Still fun school

Student.age = 50  # This introduces a new class variable
print fred.age  # Fred already had an age, so his age is still 21
# werty = Student("Werty")  # __init__ expects an age as well


Student.count = 20  # Manually update student count
# The instances don't have count variable, so they ask their class if it has one
print fred.count

# This fails because neither Fred nor Student has a mascot variable
# print fred.mascot

print fred.__dict__ # See all of Fred's attributes
print Student.__dict__ # See all of the Student attributes and methods