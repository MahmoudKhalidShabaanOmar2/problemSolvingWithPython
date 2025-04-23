# write a python program to get ten student names in the list of student names , in this condition , the system should display only student names that startwith "a" , Or "A" =>
lista_of_student_names = []
for i in range(10) :
    student_names = input(f"Please Enter The Name Of The Student {i + 1} To Store In The List Of The Student Names Is : ")
    lista_of_student_names . append(student_names)
print("The List Of The Student Names Is : ")
for j in lista_of_student_names :
    print(j)
print("The List Of The Student Names That Student Names Startwith \"A\" , Or \"a\" Is : ")
for k in lista_of_student_names : 
    if(k.startswith("A") or (k.startswith("a"))) :
        print(k)