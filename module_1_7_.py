# Исходные данные
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(students)
print(grades)
# Сортируем список студентов по алфавиту
students = sorted(students)
print(students)
# разбиваем список по каждому студенту отдельноb(создаём переменную на каждого студента)
student_0 = students[0]
student_1 = students[1]
student_2 = students[2]
student_3 = students[3]
student_4 = students[4]
# разбиваем список данных (оценки) по каждому студенту отдельно (создаём переменную по каждому студенту)
grades_0 = grades[0]
grades_1 = grades[1]
grades_2 = grades[2]
grades_3 = grades[3]
grades_4 = grades[4]
# Вычисляем среднеарифметическое для каждого студента
average_grades_0 = sum(grades_0) / len(grades_0)
average_grades_1 = sum(grades_1) / len(grades_1)
average_grades_2 = sum(grades_2) / len(grades_2)
average_grades_3 = sum(grades_3) / len(grades_3)
average_grades_4 = sum(grades_4) / len(grades_4)
# Создаём словарь успеваемости первого учеников
students_grades = {student_0: average_grades_0}
print(students_grades)
# добавляем в словарь остальных студентов
students_grades[student_1] = average_grades_1
students_grades[student_2] = average_grades_2
students_grades[student_3] = average_grades_3
students_grades[student_4] = average_grades_4
print(students_grades)
#
