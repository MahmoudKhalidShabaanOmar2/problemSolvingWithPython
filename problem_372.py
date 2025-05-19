# write a python program to get the mass of an object through the density of an object by using function method =>
density_of_object = float(input("Please Enter The Density Of An Object Is = "))
volume_of_object = float(input("Please Enter The Volume Of An Object Is = "))
def get_mass_of_object(density , volume) :
    print("The Density Of The Object Is = ",str(density))
    print("The Volume Of The Object Is = ",str(volume))
    mass_of_object = density * volume 
    print("The Mass Of The Object Is = ",str(mass_of_object))
get_mass_of_object(density_of_object , volume_of_object)