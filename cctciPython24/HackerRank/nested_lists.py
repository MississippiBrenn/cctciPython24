# Given a list of students' names and their corresponding grades, create a nested list where each sublist contains a student's name and their grade.
names = ["John", "Emma", "Sophia"]
grades = [85, 92, 85]

nestedList = [[names[i], grades[i]] for i in range(len(names))]
print(nestedList)

#Given a list of grades, identify the second lowest grade.
grades2 = [85, 92, 78, 78, 92]
unique_grades = list(set(grades))

unique_grades.sort
if len(unique_grades) >=2:
    second_lowest = unique_grades[1]
else: 
    second_lowest = None
print(second_lowest)