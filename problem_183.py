# write a python program to get age of user into years and then converted into seconds , minutes , hours , and at the end days =>
# age_of_user_into_years = int(input("please enter the age of the user into years is = "))
# print("the age of the user into years is = "+str(age_of_user_into_years)+" years")
# age_of_user_into_seconds = age_of_user_into_years * 365 * 24 * 60 * 60 
# print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
# # age_of_user_into_minutes = age_of_user_into_years * 365 * 24 * 60 
# age_of_user_into_minutes = age_of_user_into_seconds / 60
# print("the age of the user into minutes is = "+str(age_of_user_into_minutes)+" minutes")
# # age_of_user_into_hours = age_of_user_into_years * 365 * 24
# # age_of_user_into_hours = age_of_user_into_seconds / (60 * 60) 
# age_of_user_into_hours = age_of_user_into_minutes / (60)
# print("the age of the user into hours is = "+str(age_of_user_into_hours)+" hours")
# # age_of_user_into_days = age_of_user_into_years * 365 
# # age_of_user_into_days = age_of_user_into_seconds / (60 * 60 * 24)
# age_of_user_into_days = age_of_user_into_minutes / (60 * 24)
# print("the age of the user into days is = "+str(age_of_user_into_days)+"days")

age_of_user_into_years = int(input("please enter the age of the user into years is = "))
if(age_of_user_into_years > 0) :
    age_of_user_into_seconds = age_of_user_into_years * 365 * 24 * 60 * 60 
    print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
    # age_of_user_into_minutes = age_of_user_into_years * 365 * 24 * 60
    age_of_user_into_minutes = age_of_user_into_seconds / (60)
    print("the age of the user into minutes is = "+str(age_of_user_into_minutes)+" minutes")
    # age_of_user_into_hours = age_of_user_into_years * 365 * 24
    # age_of_user_into_hours = age_of_user_into_seconds / (60 * 60)
    age_of_user_into_hours = age_of_user_into_minutes / 60 
    print("tha age of the user into hours is = "+str(age_of_user_into_hours)+" hours")
    # age_of_user_into_days = age_of_user_into_years * 365 
    # age_of_user_into_days = age_of_user_into_seconds / (24 * 60 * 60)
    age_of_user_into_days = age_of_user_into_minutes / (24 * 60)
    print("the age of the user into days is = "+str(age_of_user_into_days)+" days")
else :
    print("please enter a valid user age into years to get user age into seconds , minutes , hours , and at the end days")