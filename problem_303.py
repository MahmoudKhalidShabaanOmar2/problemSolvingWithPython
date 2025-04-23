# write a python program to get ten student age in a list of student age , and condition is that , the system should display only student ages grater than 14 years , and less than 20 years => 
lista_of_student_ages = []
for i in range(10) :
    student_ages = float(input(f"Please Enter The Student Age {i + 1} Is = "))
    lista_of_student_ages . append(student_ages)
print("The List Of Student Ages Is : "+str(lista_of_student_ages))
for j in lista_of_student_ages :
    print(j)
print("The List Of Student Ages That Age Is Grater Than 14 Years , And Less Than 20 Years Is : ")
for k in lista_of_student_ages :
    if(k > 14 and k < 20) :
        print(k)