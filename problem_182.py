# write a python program to get age of the user into years , and then converted to seconds by using different functions methods =>
# age_of_user_into_years = float(input("please enter the age of the user into years is = "))
# def get_age_of_user_into_seconds(age_into_years) :
#     print("the age of the user into years is = "+str(age_into_years)+" years")
#     age_of_user_into_seconds = age_into_years *  365 * 24 * 60 * 60 
#     print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
# get_age_of_user_into_seconds(age_of_user_into_years)

# age_of_user_into_years = float(input("please enter the age of the user into years is = "))
# def get_age_of_user_into_seconds(age_into_years) :
#     print("the age of the user into years is = "+str(age_into_years)+" years")
#     if(age_into_years > 0) :
#         age_of_user_into_seconds = age_into_years * 365 * 24 * 60 * 60 
#         print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
#     else :
#         print("please enter valid user age into years to get the age into seconds")
# get_age_of_user_into_seconds(age_of_user_into_years)

# def get_age_of_user_into_seconds(age_into_years) :
#     print("the age of the user into years is = "+str(age_into_years)+" years")
#     age_of_user_into_seconds = age_into_years * 365 * 24 * 60 * 60 
#     return("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
# age_of_user_into_years = float(input("please enter the age of the user into years is = "))
# age_into_seconds = get_age_of_user_into_seconds(age_of_user_into_years)
# print(age_into_seconds)

def get_age_of_user_into_seconds(age_into_years) :
    print("the age of the user into years is = "+str(age_into_years)+" years")
    if(age_into_years > 0) :
        age_of_user_into_seconds = age_into_years * 365 * 24 * 60 * 60
        return("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
    else :
        return("please enter a valid age into years to get age into seconds")
age_of_user_into_years = float(input("please enter the age of the user into years is = "))
age_into_seconds = get_age_of_user_into_seconds(age_of_user_into_years)
print(age_into_seconds)
    