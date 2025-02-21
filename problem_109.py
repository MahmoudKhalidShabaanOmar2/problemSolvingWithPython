# write a python program to get ten name of the students from the user in a list , and display that students name in descending order with removing the frist and last student name =>
lista_of_student_names = []
for i in range(10) :
    lista_of_student_names . append(input("please enter the student names to store in the list of the student names is : "))
print("the list of the student names in the ascending (properly) order before removing the frist , and last student names is : \n")
for j in lista_of_student_names :
    print(j)
lista_of_student_names . reverse()
print("the list of the student names in the descending (reversing) order before removing the frist , and last student names is : \n")
for k in lista_of_student_names :
    print(k)
lista_of_student_names . reverse()
lista_of_student_names . pop()
lista_of_student_names . pop(0)
print("the list of the student names in the ascending (properly) order after removing the frist , and last student names is : \n")
for n in lista_of_student_names :
    print(n)
lista_of_student_names . reverse()
print("the list of the student names in the descending (reversing) order after removing the frist , and last student names is : \n")
for m in lista_of_student_names :
    print(m)