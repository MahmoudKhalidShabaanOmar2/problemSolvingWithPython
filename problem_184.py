# write a python program to get user age into years , and then converted to user age into seconds , minutes , hours , and at the end days by using function methods => 
# age_of_user_into_years = int(input("please enter the age of the user into years is = "))
# def get_age_into_sec_min_hour_day(age_into_years) :
#     print("the age of the user into years is = "+str(age_into_years)+" years")
#     age_of_user_into_seconds = age_into_years * 365 * 24 * 60 * 60
#     print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
#     # age_of_user_into_minutes = age_into_years * 365 * 24 * 60 
#     age_of_user_into_minutes = age_of_user_into_seconds / (60)
#     print("the age of the user into minutes is = "+str(age_of_user_into_minutes)+" minutes")
#     # age_of_user_into_hours = age_into_years * 365 * 24 
#     # age_of_user_into_hours = age_of_user_into_seconds / (60 * 60)
#     age_of_user_into_hours = age_of_user_into_minutes / (60)
#     print("the age of the user into hours is = "+str(age_of_user_into_hours)+" hours")
#     # age_of_user_into_days = age_into_years * 365 
#     # age_of_user_into_days = age_of_user_into_seconds / (24 * 60 * 60)
#     age_of_user_into_days = age_of_user_into_minutes / (24 * 60)
#     print("the age of the user into days is = "+str(age_of_user_into_days)+" days")
# get_age_into_sec_min_hour_day(age_of_user_into_years)

age_of_user_into_years = int(input("please enter the age of the user into years is = "))
def get_age_into_sec_min_hour_day(age_into_years) :
    print("the age into years is = "+str(age_into_years)+" years")
    if(age_into_years > 0) :
        age_of_user_into_seconds = age_into_years * 365 * 24 * 60 * 60 
        print("the age of the user into seconds is = "+str(age_of_user_into_seconds)+" seconds")
        # age_of_user_into_minutes = age_into_years * 365 * 24 * 60 * 60 
        age_of_user_into_minutes = age_of_user_into_seconds / (60)
        print("the age of the user into minutes is = "+str(age_of_user_into_minutes)+" minutes")
        # age_of_user_into_hours = age_into_years * 365 * 24 * 60
        # age_of_user_into_hours = age_of_user_into_seconds / (60 * 60)
        age_of_user_into_hours = age_of_user_into_minutes / (60)
        print("the age of the user into hours is = "+str(age_of_user_into_hours)+" hours")
        # age_of_user_into_days = age_into_years * 365 * 24 
        # age_of_user_into_days = age_of_user_into_seconds / (24 * 60 * 60)
        age_of_user_into_days = age_of_user_into_minutes / (24 * 60)
        print("the age of the user into days is = "+str(age_of_user_into_days)+" days")
    else :
        print("please enter a valid user age to get the age of the user into seconds , minutes , hours , and at the end days")
get_age_into_sec_min_hour_day(age_of_user_into_years)