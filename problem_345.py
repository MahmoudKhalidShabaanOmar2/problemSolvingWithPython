# write a python program to sort student names in the list of student in ascending order , and student names should display student names that contains only five characters =>
lista_of_student_names = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms)," Terms")
for j in range(num_of_terms) :
    student_names = input(f"Please Enter The Student Name {j + 1} Is :")
    lista_of_student_names.append(student_names)
print("The List Of All Student Names Is : ")
for i in lista_of_student_names :
    print(i)
print("The List Of All Student Names That Contains Only Five Characters Is : ")
for k in lista_of_student_names :
    if(len(k) <= 5) :
        print(k)