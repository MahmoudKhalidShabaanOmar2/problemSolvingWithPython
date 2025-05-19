# write a python program to get density of an object by using function method =>
mass_of_object = float(input("Please Enter The Mass Of An Object Is = "))
volume_of_object = float(input("Please Enter The Volume Of An Object Is = "))
def get_denstiy_of_object(mass , volume) :
    print("The Mass Of The Object Is = ",str(mass)," Kilo Grama")
    print("The Vloume Of The Object Is = ",str(volume)," Meter3")
    density_of_object = mass / volume 
    print("The Density Of The Object Is = ",str(density_of_object))
get_denstiy_of_object(mass_of_object , volume_of_object)