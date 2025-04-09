# write a python program to get list of different student marks , then find the second position of student marks , and then display all student marks =>
lista_of_different_student_marks = []
for i in range(5) :
    student_marks = int(input("please enter the different student marks to store in the list of the student marks is : "))
    lista_of_different_student_marks.append(student_marks)
print("the list of the student marks is : "+str(lista_of_different_student_marks))
print("the second student marks from the list of the different student marks is : "+str(lista_of_different_student_marks[1])+" marks")