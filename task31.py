import csv


def add_student(name, lastname, age):

    with open('students.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([name, lastname, age])


add_student('Mary', 'Brown', '20')
add_student('Pony', 'Los', '18')