# write a python program to get the list of the student names from the user , and then display them on the screen , the user be able to update any student name from the list of student names =>
number_of_users = int(input("Please Enter The Number Of Users Is = "))
print("The Number Of Users Is = ",str(number_of_users)," Users")
lista_of_student_names = []
for i in range(number_of_users):
    student_name = input(f"Please Enter The Student Name({i+1}) Is : ")
    lista_of_student_names.append(student_name)
print("The List Of The Student Names Is : ",str(lista_of_student_names))
for j in range(number_of_users):
    print(lista_of_student_names[j])
removed_student_name = input("Please Enter The Removed Student Name Is : ")
print("The Removed Student Name Is : ",removed_student_name)
lista_of_student_names.remove(removed_student_name)
print("The List Of The Student Names After Removing The Removed Student Name Is : ",str(lista_of_student_names))
for k in range(number_of_users): 
    print(lista_of_student_names[k])