# write a python program to get ten student identifies numbers in the list of the student identifies numbers , system should help to avoid duplicate identifies insertion =>
student_identifies_numbers = set()
while (len(student_identifies_numbers) < 10) :
    student_identify = input(f"please enter the identify number of the student {len(student_identifies_numbers) + 1}\\10 is : ").strip()
    if (student_identify in student_identifies_numbers) :
        print("duplicate id , please enter a valid unique student identify number")
    else :
        student_identifies_numbers . add(student_identify)
lista_of_student_identifies_numbers = list(student_identifies_numbers)
print("\nthe final list of the student identifies numbers is ")
print(lista_of_student_identifies_numbers)