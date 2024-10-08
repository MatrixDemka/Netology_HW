class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_course = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        """метод оценки лекторов"""
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def average_grade(self):
        """считаем среднюю оценку"""
        if not self.grades:
            return 0
        value = []
        for i in self.grades.values():
            value.extend(i)
        return round(sum(value)/len(value), 2)
         
    def __str__(self) -> str:
        """метод __str__ выводит тнформацио по данному классу"""
        courses_in_progress_string = ", ".join(self.courses_in_progress)  # Получаем строку курсов
        finished_courses_string = ", ".join(self.finished_courses)  #Получаем троку завершенных курсов
        result = f"Имя:{self.name}\n" \
            f"Фамилия:{self.surname}\n" \
            f"Средняя оценка за домашнее задание: {self.average_grade()}\n" \
            f"Курсы в процессе обучени: {courses_in_progress_string}\n" \
            f"Завершенные курсы: {finished_courses_string}"
        return result
    
    def __lt__(self, student):
        return self.average_grade() < student.average_grade()
      
    def __le__(self, student): 
        return self.average_grade() > student.average_grade()
    
    def __eq__(self, student):
        return self.average_grade() == student.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        """считаем среднюю оценку"""
        if not self.grades:
            return 0
        value = []
        for i in self.grades.values():
            value.extend(i)
        return round(sum(value)/len(value), 2)
    
    def __str__(self):
        result = f"Имя: {self.name} \n" \
        f"Фамилия: {self.surname} \n" \
        f"Средняя оценка за домашнее задание: {self.average_grade()}"
        return result
    
    def __lt__(self, lecturer):
        return self.average_grade() < lecturer.average_grade()
      
    def __le__(self, lecturer): 
        return self.average_grade() > lecturer.average_grade()
    
    def __eq__(self, lecturer):
        return self.average_grade() == lecturer.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """метод оценки студентов за домашнюю работу"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
    
    def __str__(self):
        result = f"Имя: {self.name} \n" \
        f"Фамилия: {self.surname}"
        return result

"""
Функция подсчета средней оценки по всем (студентам/лекторам) в рамках конкретного курса
""" 
def average_grade_on_the_course(persons, course):
    count = []
    summa =[]
    for person in persons:
        for course in person.grades.keys():
            count = len(person.grades[course])
            summa = sum(person.grades[course])
    return round(summa / count, 2)


#Создаём студентов
student1 = Student("Anna", "Karenina", 22)
student1.courses_in_progress += ["Java"]  # Первый учится на курсе Java
student1.finished_courses += ["Python"]  # Закончил курс Python

student2 = Student("Bob", "Marley", 19)
student2.courses_in_progress += ["Python"] # Второй учится на курсе Python
student2.finished_courses += ["Java"]  # Закончил курс Java

student3 = Student("Denia", "Armstrong", 18)
student3.courses_in_progress += ["Java"]  # Третий учится на курсе Java
student3.finished_courses += ["Python"]  # Закончил курс Python

#Создаём проверяющих
reviewer1 = Reviewer("Zigmund", "Freid")
reviewer1.courses_attached += ["Java"] # Закреплён за курсом Java

reviewer2 = Reviewer("Jasson", "Blue")
reviewer2.courses_attached += ["Python"] # Закреплён за курсом Python

#Создаём лекторов
lecturer = Lecturer("Anna", "Smith")
lecturer.courses_attached += ["Python"] # Закреплён за курсом Python

lecturer2 = Lecturer("Lisa", "Semenova")
lecturer2.courses_attached += ["Java"] # Закреплён за курсом Java

lecturer3 = Lecturer("Dina", "Ignatova")
lecturer3.courses_attached += ["Python", "Java"] # Закреплён за курсом Python

#Проверяющие выставляют оценки студентам
reviewer1.rate_hw(student1, "Java", 5)
reviewer1.rate_hw(student1, "Java", 8)
reviewer1.rate_hw(student1, "Java", 10)

reviewer1.rate_hw(student3, "Java", 5)
reviewer1.rate_hw(student3, "Java", 8)
reviewer1.rate_hw(student3, "Java", 10)

reviewer2.rate_hw(student2, "Python", 5)
reviewer2.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student2, "Python", 10)

reviewer2.rate_hw(student3, "Python", 3)
reviewer2.rate_hw(student3, "Python", 6)
reviewer2.rate_hw(student3, "Python", 8)

reviewer2.rate_hw(student3, "Python", 10)
reviewer2.rate_hw(student3, "Python", 4)
reviewer2.rate_hw(student3, "Python", 8)

#Студенты выставляют оценки лекторам
student1.rate_lecturer(lecturer2, "Java", 6)
student1.rate_lecturer(lecturer2, "Java", 2)
student1.rate_lecturer(lecturer2, "Java", 4)

student2.rate_lecturer(lecturer, "Python", 10)
student2.rate_lecturer(lecturer, "Python", 8)
student2.rate_lecturer(lecturer, "Python", 4)

student3.rate_lecturer(lecturer3, "Java", 10)
student3.rate_lecturer(lecturer3, "Java", 7)
student3.rate_lecturer(lecturer3, "Java", 5)

print("Поверяющий 1 выставляет оценки студенту 1")
print(student1.grades)
print()
print("Поверяющий 2 выставляет оценки студенту 2")
print(student2.grades)
print()
print("Студент 2 выставляет оценку лектору 1")
print(lecturer.grades)
print()
print("Студент 1 выставляет оценку лектору 2")
print(lecturer2.grades)
print()
print("Студент 1 выставляет оценку лектору 3")
print(lecturer3.grades)
print()
print(student1)
print()
print(reviewer1)
print()
print(lecturer)
print()
print(student1.__eq__(student2))
print(lecturer.__eq__(lecturer2))
print(student1.__lt__(student2))
print(lecturer.__le__(lecturer2))

all_student_lst = [student1, 
                   student2, 
                   student3
                   ]

all_lecturer_list = [lecturer,
                     lecturer2,
                     lecturer3
                     ]

print(f'Средняя оценка студентов - {average_grade_on_the_course(all_student_lst, "Python")}')
print(f'Средняя оценка лекторов - {average_grade_on_the_course(all_lecturer_list, "Python")}')