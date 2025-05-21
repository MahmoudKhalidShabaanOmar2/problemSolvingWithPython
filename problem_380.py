# write a python program to get the change of the velocity of an object , by givem acceleration of object , and time token by object by using function methods =>
acceleration_of_object = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
time_token_by_object = int(input("Please Enter The Time Of An Object Is = "))
def get_change_of_velocity_of_object(a_b , t_b) :
    print("The Acceleration Of An Object Is = ",str(a_b)," Meter/Second2")
    print("The Time Token By An Object Is = ",str(t_b)," Second")
    change_of_velocity_of_object = a_b * t_b 
    print("The Change Of The Velocity Of An Object Is = ",str(change_of_velocity_of_object)," Meter/Second2")
get_change_of_velocity_of_object(acceleration_of_object , time_token_by_object)