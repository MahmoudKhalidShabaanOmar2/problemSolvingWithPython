# write a python program to get the volume of an object through the density of an object by using function method =>
density_of_object = int(input("Please Enter The Density Of An Object Is = "))
mass_of_object = int(input("Please Enter The Mass Of An Object Is = "))
def get_volume_of_object(density , mass) :
    print("The Mass Of The Object Is = ",str(mass))
    print("The Density Of The Object Is = ",str(density))
    volume_of_object = density * mass 
    print("The Volume Of The Object Is = ",str(volume_of_object))
get_volume_of_object(density_of_object , mass_of_object)