# write a python program to get scale from the employer to display the salary of the employer by using this criteria =>
# employer_scale is 9 , display salary is 10000$ 
# employer_scale is 12 , display salary is 20000$ 
# employer_scale is 15 , display salary is 40000$ 
# employer_scale is 18 , display salary is 50000$
# employer_scale is 20 , display salary is 70000$ 
# employer_scale = int(input("please enter the employer scale is = "))
# def get_employer_salary(em_scale) :
#     print("the employer scale is = "+str(em_scale))
#     if(em_scale == 9) :
#         print("the salary of the employer is = 10000$ , because the employer scale is = "+str(em_scale))
#     elif(em_scale == 12) :
#         print("the salary of the employer is = 20000$ , because the employer scale is = "+str(em_scale))
#     elif(em_scale == 15) :
#         print("the salary of the employer is = 40000$ , because the employer scale is = "+str(em_scale))
#     elif(em_scale == 18) :
#         print("the salary of the employer is = 50000$ , because the employer scale is = "+str(em_scale))
#     elif(em_scale == 20) :
#         print("the salary of the employer is = 70000$ , because the employer scale is = "+str(em_scale))
#     else :
#         print("please enter one of the vaild employer scale like 9 , 12 , 15 , 18 , or 20 to display the right salary of the employer")
# get_employer_salary(employer_scale)

def get_employer_salary(em_scale) :
    print("the employer scale is = "+str(em_scale))
    if(em_scale == 9) :
        return("the salary of the employer is = 10000$ , because the employer scale is = "+str(em_scale))
    elif(em_scale == 12) :
        return("the salary of the employer is = 20000$ , because the employer scale is = "+str(em_scale))
    elif(em_scale == 15) :
        return("the salary of the employer is = 40000$ , because the employer scale is = "+str(em_scale))
    elif(em_scale == 18) :
        return("the salary of the employer is = 50000$ , because the employer scale is = "+str(em_scale))
    elif(em_scale == 20) :
        return("the salary of the employer is = 70000$ , because the employer scale is = "+str(em_scale))
    else :
        return("please enter one of the valid employer scale like 9 , 12 , 15 , 18 , or 20 to display the salary of the employer")
employer_scale = int(input("please enter the employer scale is = "))
get_salary = get_employer_salary(employer_scale)
print(get_salary)