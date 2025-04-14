# write a python program to get five student names in a tuple , and then check if the frist student name is the same of the last student name from the tuple of the student names => 
lista_of_student_names = []
for i in range(5) :
    student_names = input(f"Please Enter The Student Name {i + 1} To Store In The List Of The Student Name Is : ")
    lista_of_student_names.append(student_names)
print("\nThe List Of The Student Names Is : ")
print(lista_of_student_names)    
tuples_of_student_names = tuple(lista_of_student_names)
print("\nThe Tuple Of The Student Names Is : ")
print(tuples_of_student_names)
if(tuples_of_student_names[0] == tuples_of_student_names[-1]) :
    print("The Frist Name Of The Student Is The Same Of The Last Name Of Student Name From The Tuple Of The Student Name")
else :
    print("The Frist Name Of The Student Is Not The Same Of The Last Name Of The Student Name From The Tuple Of The Student Name")