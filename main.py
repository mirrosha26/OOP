class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        courses_pr = ", ".join(map(str, self.courses_in_progress))
        courses_fin = ", ".join(map(str, self.finished_courses))
        return_str = f"\nИмя: {self.name}\n"
        return_str += f"Фамилия: {self.surname}\n"
        return_str += f"Средняя оценка за домашние задания: {self.arithmetic_mean_grate()}\n"
        return_str += f"Курсы в процессе изучения: {courses_pr}\n"
        return_str += f"Завершенные курсы: {courses_fin}"
        return return_str

    def grate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return True
        else:
            print("Ошибка")
            return False

    def arithmetic_mean_grate(self):
        if self.grades == {}:
            return None
        sum = 0
        len = 0
        for course_grades in self.grades.values():
            for grades in course_grades:
                len += 1
                sum += grades
        arithmetic_mean = sum / len
        return round(arithmetic_mean, 2)

    def check_grate(self, other):
        if isinstance(other, Student) and (self.grades != {} or other.grades != {}):
            return True
        return False

    def __eq__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() == other.arithmetic_mean_grate()

    def __ne__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() != other.arithmetic_mean_grate()

    def __gt__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() > other.arithmetic_mean_grate()

    def __lt__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() < other.arithmetic_mean_grate()

    def __ge__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() >= other.arithmetic_mean_grate()

    def __le__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() <= other.arithmetic_mean_grate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return_str = f"\nИмя: {self.name}\n"
        return_str += f"Фамилия: {self.surname}\n"
        return_str += f"Средняя оценка за домашние задания: {self.arithmetic_mean_grate()}\n"
        return return_str

    def arithmetic_mean_grate(self):
        if self.grades == {}:
            return None
        sum = 0
        len = 0
        for course_grades in self.grades.values():
            for grades in course_grades:
                len += 1
                sum += grades
        arithmetic_mean = sum / len
        return round(arithmetic_mean, 2)

    def check_grate(self, other):
        if isinstance(other, Lecturer) and (self.grades != {} or other.grades != {}):
            return True
        return False

    def __eq__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() == other.arithmetic_mean_grate()

    def __ne__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() != other.arithmetic_mean_grate()

    def __gt__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() > other.arithmetic_mean_grate()

    def __lt__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() < other.arithmetic_mean_grate()

    def __ge__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() >= other.arithmetic_mean_grate()

    def __le__(self, other):
        if self.check_grate(other):
            return self.arithmetic_mean_grate() <= other.arithmetic_mean_grate()


class Reviewer(Mentor):
    def grate_student(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and grade in range(
                1, 11, 1):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return True
        else:
            print('Ошибка')
            return False

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}"


student_1 = Student('Иван', 'Солодов', 'man')
student_2 = Student('Миша', 'Мирошников', 'man')

reviewer_1 = Reviewer("Миша", "Шишкин")
reviewer_2 = Reviewer("Леша", "Иванов")

lecture_1 = Lecturer('Иван', 'Иванов')
lecture_2 = Lecturer('Алексей', 'Петров')

student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['СУБД']

lecture_1.courses_attached += ['Python']
lecture_2.courses_attached += ['Python']
lecture_2.courses_attached += ['СУБД']

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Python']

student_1.finished_courses += ['UX/UI']
student_2.finished_courses += ['UX/UI']

reviewer_1.grate_student(student_2, 'Python', 5)
reviewer_1.grate_student(student_2, 'Python', 4)

reviewer_2.grate_student(student_1, 'Python', 5)
reviewer_2.grate_student(student_1, 'Python', 5)

student_1.grate_lecturers(lecture_1, 'Python', 10)
student_1.grate_lecturers(lecture_1, 'Python', 10)

student_2.grate_lecturers(lecture_2, 'Python', 10)
student_2.grate_lecturers(lecture_2, 'Python', 9)
student_2.grate_lecturers(lecture_2, 'СУБД', 10)
print(student_1)
print(student_2)
print(lecture_1)
print(lecture_2)
print(reviewer_1)
print(reviewer_2)

students = [student_1, student_2]
lectures = [lecture_1, lecture_2]
print()

print(f"[lecture_1 == lecture_2] is {lecture_1 == lecture_2}")
print(f"[lecture_1 != lecture_2] is {lecture_1 != lecture_2}")
print(f"[lecture_1 <= lecture_2] is {lecture_1 <= lecture_2}")
print(f"[lecture_1 >= lecture_2] is {lecture_1 >= lecture_2}")
print(f"[lecture_1 < lecture_2] is {lecture_1 < lecture_2}")
print(f"[lecture_1 > lecture_2] is {lecture_1 > lecture_2}")

print(f"\n[student_1 == student_2] is {student_1 == student_2}")
print(f"[student_1 != student_2] is {student_1 != student_2}")
print(f"[student_1 <= student_2] is {student_1 <= student_2}")
print(f"[student_1 >= student_2] is {student_1 >= student_2}")
print(f"[student_1 < student_2] is {student_1 < student_2}")
print(f"[student_1 > student_2] is {student_1 > student_2}")

'''
Получается, что одна функция реализует подсчет как для всех лекторов,
так и для студентов в рамках одного курса
'''


def get_grade_for_course(not_reviewers, course):
    all = 0
    size = 0
    for not_reviewer in not_reviewers:
        if not_reviewer.grades.get(course) != None:
            grades = not_reviewer.grades.get(course)
            all += sum(grades)
            size += len(grades)
    if len != 0:
        return round(all / size, 2)
    return None


print()
print(get_grade_for_course(students, "Python"))
print(get_grade_for_course(lectures, "СУБД"))
