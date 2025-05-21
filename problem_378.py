# write a python program to get an acceleration of an object by using change of velocity , and time =>
starting_of_velocity_of_object = int(input("Please Enter The Starting Of Velocity Of An Object Into Meter/Second Is = "))
ending_of_velocity_of_object = int(input("Please Enter The Ending Of Velocity Of An Object Into Meter/Second Is = "))
time_of_object = int(input("Please Enter The Time Of The Object Into Second Is = "))
def getting_acceleration_of_object(s_v , e_v , t) :
    print("The Starting Velocity Of An Object Is = ",str(s_v)," Meter/Second")
    print("The Ending Of Velocity Of An Object Is = ",str(ending_of_velocity_of_object)," Meter/Second")
    change_of_velocity_of_object = e_v - s_v 
    print("The Change Of The Velocity Of An Object Is = ",str(change_of_velocity_of_object)," Meter/Second")
    acceleration_of_object = change_of_velocity_of_object / t 
    print("The Acceleration Of An Object Is = ",str(acceleration_of_object)," Meter/Second2")
getting_acceleration_of_object(starting_of_velocity_of_object , ending_of_velocity_of_object , time_of_object)