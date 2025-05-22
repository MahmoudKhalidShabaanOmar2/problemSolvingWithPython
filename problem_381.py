# write a python program to get the force of an object which have mass of an object , and acceleration of an object by using function method =>
# massOfObject = int(input("Please Enter The Mass Of An Object Into Kilograma Is = "))
# acceleration_of_object = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
# def get_force_of_object(m_b , a_b) :
#     print("The Mass Of An Object Is = ",str(m_b)," Kilo Grama")
#     print("The Acceleration Of An Object Is = ",str(a_b)," Meter/Second2")
#     force_of_object = m_b * a_b 
#     print("The Force Of An Object Is = ",str(force_of_object)," Newoton")
# get_force_of_object(massOfObject , acceleration_of_object)

def get_force_of_object(m_b , a_b) :
    print("The Mass Of An Object Is = ",str(m_b)," Kilo Grama")
    print("The Acceleration Of An Object Is = ",str(a_b))
    force_of_object = m_b * a_b 
    return("The Force Of An Object Is = "+str(force_of_object)+" Newoton")
mass_of_object = int(input("Please Enter The Mass Of An Object Into Kilo Grama Is = "))
acceleration_of_object = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
displaying_force_of_object = get_force_of_object(mass_of_object , acceleration_of_object)
print(displaying_force_of_object)