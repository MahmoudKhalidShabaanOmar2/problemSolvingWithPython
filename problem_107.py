# write a python program to get ten name of the students from the user in a list , and display that students name in descending order =>
lista_of_student_names = []
# for i in range(10) :
    # lista_of_student_names . append(input("please enter the name of the student to store in the list of the student names is : "))
lista_of_student_names = [input("please enter the name of the student to store in the list of the student name is : ") for i in range(10)]
print("the list of the student name in the ascending (properly) order is : \n")
for j in lista_of_student_names : 
    print(j)
print("the list of the student name in the descending (reversing) order is : \n")
lista_of_student_names . reverse()
for k in lista_of_student_names :
    print(k)