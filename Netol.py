def GT (a,b):
    print("Лучшая оценка у",end=" ")
    if (a>b):
        print(a.name,a.surname)
    else:
        print(b.name,b.surname)

def counting(grad,cours_in_prog):
    k=0
    sr_grad=0
    if len(grad) != 0:
        for gr in grad[cours_in_prog[0]]:
            k=k+1
            sr_grad=sr_grad+gr
        sr=sr_grad/k
    else:
        sr=0
    return sr

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sr=counting(self.grades,self.courses_in_progress)
        return f"распечатать(some_student) \nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sr}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

    def __gt__(self, other):
        return  counting(self.grades,self.courses_in_progress)>counting(other.grades,other.courses_in_progress)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"распечатать(some_mentor) \nИмя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        sr=counting(self.grades,self.courses_attached)
        return f"печать(some_lecturer) \nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sr}"

    def __gt__(self, other):
        return  counting(self.grades,self.courses_attached)>counting(other.grades,other.courses_attached)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"распечатать(some_reviewer) \nИмя: {self.name}\nФамилия: {self.surname}"

best_student = Student('Ruoy', 'Eman', 'your_gender')
student1 = Student('Nik', 'Kin', 'male')
student1.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['C++']

mentor1 = Mentor('Vlad', 'Mel')
mentor2 = Mentor('Iva', 'Glu')

rewiwer1 = Reviewer('Some', 'Buddy')
rewiwer1.courses_attached += ['Python']
rewiwer2 = Reviewer('Some', 'Buddy')
rewiwer2.courses_attached += ['Python']

rewiwer1.rate_hw(best_student, 'Python', 10)
rewiwer1.rate_hw(best_student, 'Python', 9)
rewiwer1.rate_hw(student1, 'Python', 8)
rewiwer1.rate_hw(student1, 'Python', 7)

lecturer1 = Lecturer('Som', 'Bud')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('Zom', 'Byd')
lecturer2.courses_attached += ['Python']

best_student.rate(lecturer1, 'Python', 6)
best_student.rate(lecturer2, 'Python', 5)

student1.rate(lecturer1, 'Python', 4)
student1.rate(lecturer2, 'Python', 3)



print(best_student)
print()
print(rewiwer1)
print()
print(lecturer1)
print()
print(mentor1)
print()
GT(best_student,student1)
GT(lecturer1,lecturer2)
print()

List=[]
list_name=[]
list_zn=[]
List.append(best_student)
List.append(student1)
list_sl=[]

for obj in List:
    q=obj.grades
    for key, value in q.items() :
        list_sl.append(key)
list_sl=list(set(list_sl))


for lsl in list_sl:
    for obj in List:
        q=obj.grades
        for key, value in q.items() :
            if lsl == key:
                list_zn.append(counting(obj.grades,obj.courses_in_progress))
    print(lsl,sum(list_zn)/len(list_zn),"средняя оценка Студентов")

List=[]
list_name=[]
list_zn=[]
List.append(lecturer1)
List.append(lecturer2)
list_sl=[]

for obj in List:
    q=obj.grades
    for key, value in q.items() :
        list_sl.append(key)
list_sl=list(set(list_sl))


for lsl in list_sl:
    for obj in List:
        q=obj.grades
        for key, value in q.items() :
            if lsl == key:
                list_zn.append(counting(obj.grades,obj.courses_attached))
    print(lsl,sum(list_zn)/len(list_zn),"средняя оценка Лектора")