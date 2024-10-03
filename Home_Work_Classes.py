class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
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
    
    def __eq__(self, student: object) -> bool:
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
    
    def __eq__(self, lecturer: object) -> bool:
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
        
        

#  Создаём двух студентов
student1 = Student("Anna", "Karenina", 22)
student1.courses_in_progress += ["Java"] # Первый учится на курсе Java
student1.finished_courses += ["Python"]

student2 = Student("Bob", "Marley", 19)
student2.courses_in_progress += ["Python"] # Второй учится на курсе Python

#  Создаём двух проверяющих
reviewer1 = Reviewer("Zigmund", "Freid")
reviewer1.courses_attached += ["Java"] # Закреплён за курсом Java

reviewer2 = Reviewer("Jasson", "Blue")
reviewer2.courses_attached += ["Python"] # Закреплён за курсом Python

#  Создаём двух лекторов
lecturer = Lecturer("Anna", "Smith")
lecturer.courses_attached += ["Python"] # Закреплён за курсом Python

lecturer2 = Lecturer("Lisa", "Semenova")
lecturer2.courses_attached += ["Java"] # Закреплён за курсом Java

#  Проверяющий 1 выставляет оценку студенту 1
reviewer1.rate_hw(student1, "Java", 5)
reviewer1.rate_hw(student1, "Java", 8)
reviewer1.rate_hw(student1, "Java", 10)

#  Проверяющий 2 выставляет оценку студенту 2
reviewer2.rate_hw(student2, "Python", 5)
reviewer2.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student2, "Python", 10)

# Студент 1 выставляет оценку лектору 2
student1.rate_lecturer(lecturer2, "Java", 6)
student1.rate_lecturer(lecturer2, "Java", 2)
student1.rate_lecturer(lecturer2, "Java", 4)

#  Студент 2 выставляет оценку лектору 1
student2.rate_lecturer(lecturer, "Python", 10)
student2.rate_lecturer(lecturer, "Python", 8)
student2.rate_lecturer(lecturer, "Python", 4)

print("Поверяющий 1 выставляет оценки студенту 1")
print(student1.grades)

print("Поверяющий 2 выставляет оценки студенту 2")
print(student2.grades)

print("Студент 2 выставляет оценку лектору 1")
print(lecturer.grades)

print("Студент 1 выставляет оценку лектору 2")
print(lecturer2.grades)

print(student1)
print(reviewer1)
print(lecturer)

print(student1.__eq__(student2))
print(lecturer2.__eq__(lecturer))