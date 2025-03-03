# write a python program to get age of the user in years , and then converted age into seconds =>
# age_of_user_into_years = float(input("please enter the age of the user into years is = "))
# print("the age of the user into years is = "+str(age_of_user_into_years)+" years")
# age_of_user_into_seconds = age_of_user_into_years * 365 * 24 * 60 * 60 
# print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")

age_of_user_into_years = float(input("please enter the age of the user into years is = "))
print("the age of the user into years is = "+str(age_of_user_into_years)+" years")
if(age_of_user_into_years > 0) :
    age_of_user_into_seconds = age_of_user_into_years * 365 * 24 * 60 * 60 
    print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
else :
    print("please enter a valid user age into years to get the age of the user into seconds")