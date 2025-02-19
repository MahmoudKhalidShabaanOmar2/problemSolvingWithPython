# write a python program to get scale from the employer to display the salary of the employer by using this criteria =>
# employer_scale is 9 , display salary is 10000$ 
# employer_scale is 12 , display salary is 20000$ 
# employer_scale is 15 , display salary is 40000$ 
# employer_scale is 18 , display salary is 50000$
# employer_scale is 20 , display salary is 70000$ 
employer_scale = int(input("please enter the employer scale is = "))
print("the employer scale is = "+str(employer_scale))
if(employer_scale == 9) :
    print("the salary of the employer is = 10000$ , because the employer scale is = "+str(employer_scale))
elif(employer_scale == 12) :
    print("the salary of the employer is = 20000$ , because the employer scale is = "+str(employer_scale))
elif(employer_scale == 15) :
    print("the salary of the employer is = 40000$ , because the employer scale is = "+str(employer_scale))
elif(employer_scale == 18) :
    print("the salary of the employer is = 50000$ , because the employer scale is = "+str(employer_scale))
elif(employer_scale == 20) :
    print("the salary of the employer is = 70000$ , because the employer scale is = "+str(employer_scale))
else :
    print("please enter one of the valid employer scale like 9 , 12 , 15 , 18 , or 20 to display the right salary of the employer")