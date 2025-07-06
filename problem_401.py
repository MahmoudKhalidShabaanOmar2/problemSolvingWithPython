# write a python program to get the temrature into centigrade , and then get the temprature into the kelvin , and fahrenheit =>
temprature_into_centigrade = float(input("Please Enter The Temprature Into The Centigrade Is = "))
print("The Temprature Into The Centigrade Is = ",str(temprature_into_centigrade)," Centigrade")
temprature_into_fahrenheit = (temprature_into_centigrade * 9/5) + 32
print("The Temprature Into Fahrenheit Is = ",str(temprature_into_fahrenheit)," Fahrenheit")
temprature_into_kelvin = temprature_into_centigrade + 273.15
print("The Temprature Into The Kelvin Is = ",str(temprature_into_kelvin)," Kelvin")