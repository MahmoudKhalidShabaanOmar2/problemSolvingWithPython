# write a python program to get the temprature into the kelvin , and then converted into the fahrenheit , and centigrade =>
temprature_into_kelvin = float(input("Please Enter The Temprature Into The Kelvin Is = "))
print("The Temprature Into The Kelvin Is = ",str(temprature_into_kelvin)," Kelvin")
temprature_into_centigrade = temprature_into_kelvin - 273.15
print("The Temprature Into The Centigrade Is = ",str(temprature_into_centigrade)," Centigrade")
temprature_into_fahrenheit = (temprature_into_centigrade * 9/5) + 32
print("The Temprature Into The Centigrade Is = ",str(temprature_into_fahrenheit)," Fahrenheit")