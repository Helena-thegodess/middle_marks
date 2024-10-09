students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
middle_marks_Aaron = grades[0] = sum(grades[0]) / len(grades[0])
middle_marks_Bilbo = grades[1] = sum(grades[1]) / len(grades[1])
middle_marks_Johhny = grades[2] = sum(grades[2]) / len(grades[2])
middle_marks_Khendrik = grades[3] = sum(grades[3]) / len(grades[3])
middle_marks_Steve = grades[4] = sum(grades[4]) / len(grades[4])
students = list(students)
students = sorted(['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'])
answer = {students[0]: middle_marks_Aaron, students[1]: middle_marks_Bilbo, students[2]: middle_marks_Johhny, students[3]: middle_marks_Khendrik, students[4]: middle_marks_Steve}
print(answer)