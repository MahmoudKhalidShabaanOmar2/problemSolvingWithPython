# write a python program to get the mass of an object , which have force of object , and acceleration of an object by using function method =>
# force_of_object = int(input("Please Enter The Force Of An Object Into Newoton Is = "))
# acceleration_of_object = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
# def get_mass_of_object(f_b , a_b) :
#     print("The Force Of An Object Is = ",str(f_b)," Newoton")
#     print("The Acceleration Of An Object Is = ",str(a_b)," Meter/Second2")
#     mass_of_object = f_b / a_b 
#     print("The Mass Of An Object Is = ",str(mass_of_object)," Kilo Grama")
# get_mass_of_object(force_of_object , acceleration_of_object)

def get_mass_of_object(f_b , a_b) :
    print("The Force Of An Object Is = ",str(f_b)+" Newoton")
    print("The Acceleration Of An Object Is = ",str(a_b)," Meter/Second2")
    mass_of_object = f_b / a_b 
    return("The Mass Of An Object Is = "+str(mass_of_object)+" Kilo Grama")
force_of_object = int(input("Please Enter The Force Of An Object Into Newoton Is = "))
acceleration_of_object = int(input("Please Enter The Acceleration Of An Object Into Meter/Second Is = "))
displaying_mass_of_object = get_mass_of_object(force_of_object , acceleration_of_object)
print(displaying_mass_of_object)