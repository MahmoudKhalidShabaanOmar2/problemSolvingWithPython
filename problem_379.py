# write a python program to get time token by an object , bu given the acceleration Of An Object , and change of velocity of an object by using function method =>
starting_of_velocity_of_object = int(input("Please Enter The Starting Of The Velocity Of An Object Into Meter/Second Is = "))
ending_of_velocity_of_object = int(input("Please Enter The Ending Of The Velocity Of An Object Into Meter/Second Is = "))
acceleration_of_object = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
def get_time_token_by_object(s_v_o , e_v_o , a_o) :
    print("The Starting Of The Velocity Of An Object Is = ",s_v_o," Meter/Second")
    print("The Ending Of The Velocity Of An Object Is = ",str(e_v_o)," Meter/Second")
    change_of_velocity_of_object = e_v_o - s_v_o 
    print("The Change Of The Velocity Between Starting Velocity Of An Object , And Ending Velocity Of An Object Is = ",str(change_of_velocity_of_object)," Meter/Second")
    print("The Acceleraation Of An Object Is = ",str(acceleration_of_object)," Meter/Second2")
    time_token_by_object = change_of_velocity_of_object / acceleration_of_object 
    print("The Time Token By Object Is = ",str(time_token_by_object)," Second2")
get_time_token_by_object(starting_of_velocity_of_object , ending_of_velocity_of_object , acceleration_of_object)