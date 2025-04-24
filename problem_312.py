# write a python program to find the time taken by an object having velocity difference "DV" , and acceleration "A" , get velocity , and acceleration from the user => 
starting_velocity_of_object = int(input("Please Enter The Starting Velocity Of An Object Into Meter/Second Is = "))
ending_velocity_of_object = int(input("Please Enter The Ending Velocity Of An Object Into Meter/Second Is = "))
print("The Starting Velocity Of An Object Is = ",str(starting_velocity_of_object)+" Meter/Second")
print("The Ending Velocity Of An Object Is = ",str(ending_velocity_of_object)+" Meter/Second")
difference_between_velocity_of_object = ending_velocity_of_object - starting_velocity_of_object 
print("The Difference Between The Velocity Of An Object Is = ",str(difference_between_velocity_of_object)+" Meter/Second")
acceleration_of_object = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
print("The Acceleration Of An Object Is = ",str(acceleration_of_object)," Meter/Second2")
time_token_by_object_into_second = difference_between_velocity_of_object / acceleration_of_object 
print("The Time Token By Object Is = ",str(time_token_by_object_into_second)+" Second")