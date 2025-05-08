# write a python program to sort students names in the descending order in the list and you should put . at the end of every student name =>
lista_of_student_names = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of The Terms Is = ",str(num_of_terms)," Terms")
for i in range(num_of_terms) :
    student_names = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
    lista_of_student_names.append(student_names)
print("The List Of The Student Names In The Ascending (Properly) Order Is : ")
for k in lista_of_student_names :
    print(k)
# lista_of_student_names.sort(reverse = True)
lista_of_student_names . reverse()
print("The List Of The Student Names In The Descending (Reversing) Order Is : ")
for j in lista_of_student_names :
    print(j+".")