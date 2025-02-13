# write a python program to get total marks of six subjects from the user , and then get the total marks , average  of the total marks of the all subjects by using function =>
# physics = float(input("please enter the total marks of the physics is = "))
# chemical = float(input("please enter the total marks of the chemical is = "))
# mathmaticas = float(input("please enter the total marks of the mathmaticas is = "))
# programming = float(input("please enter the total marks of the intorduction to programming is = "))
# computer_science = float(input("please enter the total marks of the computer science is = "))
# artifical_inteligence = float(input("please enter the total marks of the artifical inteligence is = "))
# def get_total_average_of_total_marks_of_all_subjects(phys , chem , math , prog , cs , ai) :
#     print("the total marks of the all subjects is : \n")
#     print("the total marks of the physics is = "+str(phys)+" marks")
#     print("the total marks of the chemical is = "+str(chem)+" marks")
#     print("the total marks of the mathmaticas is = "+str(math)+" marks")
#     print("the total marks of the introduction to programming is = "+str(prog)+" marks")
#     print("the total marks of the introduction to computer science is = "+str(cs)+" marks")
#     print("the total marks of the artifical inteligence is = "+str(ai)+" marks")
#     total_marks_of_all_subjects = phys + chem + math + prog + cs + ai
#     print("the total marks of the all subjects is = "+str(total_marks_of_all_subjects)+" marks")
#     average_of_total_marks_of_all_subjects = total_marks_of_all_subjects / 6 
#     print("the average of the total marks of the all subjects is = "+str(average_of_total_marks_of_all_subjects)+" marks")
# get_total_average_of_total_marks_of_all_subjects(physics , chemical , mathmaticas , programming , computer_science , artifical_inteligence)

def get_total_average_of_total_marks_of_all_subjects(phys , chem , math , prog , cs , ai) :
    print("the total marks of the physics is = "+str(phys)+" marks")
    print("the total marks of the chemical is = "+str(chem)+" marks")
    print("the total marks of the mathmaticas is = "+str(math)+" marks")
    print("the total marks of the introduction to programming is = "+str(prog)+" marks")
    print("the total marks of the introduction to computer science is = "+str(cs)+" marks")
    print("the total marks of the artifical inteligence is = "+str(ai)+" marks")
    total_marks_of_all_subjects = phys + chem + math + prog + cs + ai 
    print("the total marks of the all subjects is = "+str(total_marks_of_all_subjects)+" marks")
    average_of_total_marks_of_all_subjects = total_marks_of_all_subjects / 6 
    return("the average of the total marks of the all subjects is = "+str(average_of_total_marks_of_all_subjects)+" marks")
physics = float(input("please enter the total marks of the physics is = "))
chemical = float(input("please enter the total marks of the chemical is = "))
mathmaticas = float(input("please enter the total marks of the mathmaticas is = "))
programming = float(input("please enter the total marks of the introduction to programming is = "))
computer_science = float(input("please enter the total marks of the introduction to computer science is = "))
artifical_inteligence = float(input("please enter the total marks of the artifical inteligence is = "))
total_marks_and_average_of_all_subjects = get_total_average_of_total_marks_of_all_subjects(physics , chemical , mathmaticas , programming , computer_science , artifical_inteligence)
print(total_marks_and_average_of_all_subjects)