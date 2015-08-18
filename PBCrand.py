import random

def get_students():
    bootcampParticipants = [ "Andrea", "Ankur", "Anne", "Astika", "Carlo", 
                             "Dina", "Emily", "Eric", "Hadrien", "Keshav",
                             "Laura", "Lynell", "Max", "Molly", "Neera", 
                             "Pooja", "Proxima", "Reema", "Richa", "Saikiran",
                             "Sasha", "Shirish" ]
    return bootcampParticipants[:]

def get_rand_student(students):
    rand = random.randint(0,len(students)-1)
    return students[rand], rand

def get_rand_pairs():
    students = get_students()
    while len(students) > 0:
        rand1 = random.randint(0,len(students)-1)
        student1 = students[rand1]
        students.pop(rand1)
        rand2 = random.randint(0,len(students)-1)
        student2 = students[rand2]
        students.pop(rand2)
        print(60*" "+"{0} & {1}".format(student1, student2))


def main():
    students = get_students()
    while True:
        if len(students) == 0:
            print("That's all the students.")
            break
        watcha_want = raw_input("Watcha want? [ enter for 1 or type 'pairs' ] ")
        if watcha_want == "":
            student, rand = get_rand_student(students)
            print 60*" "+student
            students.pop(rand)
        elif watcha_want == "pairs":
            get_rand_pairs()
        else:
            break
                    
    
    


if __name__ == "__main__":
    main()
