# write a python program to find the difference between velocity of an object (change of velocity of an object) , and getting acceleration of object , and time token by object into second from the user => 
accelerationOfObject = int(input("Please Enter The Acceleration Of An Object Into Meter/Second2 Is = "))
timeTokenByObject = int(input("Please Enter The Time Token By An Object Is = "))
print("The Acceleration Of An Object Is = ",str(accelerationOfObject)+" Meter/Second2")
print("The Time Token By An Object Is = ",str(timeTokenByObject)," Second")
differenceBetweenVelocityOfObject = accelerationOfObject * timeTokenByObject 
print("The Difference Between Velocity Of An Object Is = ",str(differenceBetweenVelocityOfObject)+" Meter/Second")