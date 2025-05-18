# write a python program to get student age in a list of student age , and condition is that , the system should display only student ages that grater than 14 years , and less than 20 years by using function method =>
# lista_of_student_ages = []
# numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
# for stud_age in range(numbers_of_terms) :
#     student_ages = float(input(f"Please Enter The Student Age {stud_age + 1} Is = "))
#     lista_of_student_ages.append(student_ages)
# def get_list_of_student_ages(list_of_stud_ages) :
#     print("The List Of The Student Ages Is : ",str(list_of_stud_ages))
#     for age in list_of_stud_ages :
#         print(age)
#     print("The List Of Students Ages That Grater Than 14 , And Less Than 20 Is : ")
#     for k in list_of_stud_ages :
#         if((k > 14) and (k < 20)) :
#             print(k)
# get_list_of_student_ages(lista_of_student_ages)

def get_list_of_students_ages(list_of_stud_ages) :
    print("The List Of The Student Ages Is : ")
    for age in list_of_stud_ages : 
        print(age)
    print("The List Of The Student Names That Grater Than 14 , And Less Than 20 Is : ") 
    for j in list_of_stud_ages :
        if((j > 14) and (j < 20)) :
            print(j)
    return("")
lista_of_student_ages = []
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
for i in range(numbers_of_terms) :
    student_ages = float(input(f"Please Enter The Student Age {i + 1} Is = "))
    lista_of_student_ages.append(student_ages)
displaying_list_of_student_ages = get_list_of_students_ages(lista_of_student_ages)
print(displaying_list_of_student_ages)