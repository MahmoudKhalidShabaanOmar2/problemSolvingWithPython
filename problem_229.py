# write a python program to get six identify numbers of students as input and display in descending order =>
# lista_of_student_identify_numbers = []
# # for i in range(6) :
# #     student_identify_numbers = int(input("please enter the student identify numbers to store in the list of the student identify numbers is : "))
# #     lista_of_student_identify_numbers . append(student_identify_numbers)
# lista_of_student_identify_numbers = [int(input("please enter the student identify numbers to store in the list of the student identify numbers is : ")) for i in range(6)]
# print("the list of the student identify numbers in the ascending (properly) sequence is : "+str(lista_of_student_identify_numbers))
# for j in lista_of_student_identify_numbers :
#     print("\""+str(j)+"\"")
# lista_of_student_identify_numbers . reverse()
# print("the list of the student identify numbers in the descending (reversing) sequence is : "+str(lista_of_student_identify_numbers))
# for k in lista_of_student_identify_numbers : 
#     print("\""+str(k)+"\"")

lista_of_student_identify_numbers = []
# for i in range(6) :
#     student_identify_numbers = int(input("please enter the student identify numbers to store in the list of student identify numbers is : "))
#     lista_of_student_identify_numbers . append(student_identify_numbers)
lista_of_student_identify_numbers = [int(input("please enter the student identify numbers to store in the list of the student identify number is : ")) for i in range(6)]
print("the list of the student identify numbers in the ascending (properly) sequence is : "+str(lista_of_student_identify_numbers))
for j in lista_of_student_identify_numbers : 
    print("\""+str(j)+"\"")
lista_of_student_identify_numbers . sort(reverse = True) 
print("the list of the student identify numbers in the descending (reversing) sequence is : "+str(lista_of_student_identify_numbers))
for k in lista_of_student_identify_numbers : 
    print("\""+str(k)+"\"")