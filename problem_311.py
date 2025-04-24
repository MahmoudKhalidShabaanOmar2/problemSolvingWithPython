# write a python program to find the acceleration of an object having velocitey in v , and time in t =>
starting_velocity_of_object = int(input("Please Enter The Starting Velocity Of An Object Into Meter/Second Is = "))
ending_velocity_of_object = int(input("Please Enter The Ending Velocity Of An Object Into Meter/Second Is = "))
print("The Starting Velocity Of An Object Is = ",str(starting_velocity_of_object)+" Meter/Second")
print("The Ending Velocity Of An Object Is = ",str(ending_velocity_of_object)+" Meter/Second")
change_of_velocity_of_object = ending_velocity_of_object = starting_velocity_of_object 
print("The Change Of The Velocity Of An Object Is = ",change_of_velocity_of_object," Meter/Second")
time_into_second = int(input("Please Enter The Time Into Second Is = "))
print("The Time Into Second Is = ",str(time_into_second)," Second")
acceleration_of_object = change_of_velocity_of_object / time_into_second 
print("The Acceleration Of An Object Is = ",str(acceleration_of_object)," Meter/Second2")