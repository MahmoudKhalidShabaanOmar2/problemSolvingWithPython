# write a python program to find the force of man on an object , which have mass , and acceleration of an object from the user => 
massOfObject = int(input("Please Enter The Mass Of An Object Into Kilo Grama Is = "))
accelerationOfObject = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
print("The Mass Of An Object Is = ",str(massOfObject)," Kilograma")
print("The Acceleration Of An Object Is = ",str(accelerationOfObject)," Meter/Seconds2")
forceOfObject = massOfObject * accelerationOfObject 
print("The Force Of An Object Is = ",str(forceOfObject)+" Newoton")