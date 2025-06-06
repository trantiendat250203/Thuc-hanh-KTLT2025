import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]

students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

sorted_students = np.sort(students, order='height')

print("Sorted by height:")
print(sorted_students)
print ("sinh vien: Tran Van Tien Dat")
print ("Mssv: 235752020710004")