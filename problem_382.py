# write a python program to get the acceleration of an object , which have an force of an object , and mass of an object by using function method =>
# force_of_object = int(input("Please Enter The Force Of An Object Into Newoton Is = "))
# mass_of_object = int(input("Please Enter The Mass Of An Object Into Kilo Grama Is = "))
# def get_acceleration_of_object(f_b , m_b) :
#     print("The Force Of An Object Is = ",str(f_b)," Newoton")
#     print("The Mass Of An Force Is = ",str(m_b)," Kilo Grama")
#     acceleration_of_object = f_b / m_b
#     print("The Acceleration Of An Object Is = ",str(acceleration_of_object)," Meter/Second2")
# get_acceleration_of_object(force_of_object , mass_of_object)

def get_acceleration_of_object(f_b , m_b) :
    print("The Force Of An Object Is = ",str(f_b)," Newoton")
    print("The Mass Of An Object Is = ",str(m_b)," Kilo Grama")
    acceleration_of_object = f_b / m_b 
    return("The Acceleration Of An Object Is = "+str(acceleration_of_object)+" Meter/Second2")
force_of_object = int(input("Please Enter The Force Of An Object Into Newoton Is = "))
mass_of_object = int(input("Please Enter The Mass Of An Object Is = "))
displaying_acceleration_of_object = get_acceleration_of_object(force_of_object , mass_of_object)
print(displaying_acceleration_of_object)