# write a python program to get temoerature in fahrenheit , to convert into entigrade , and kelvin =>
temp_into_fahrenheit = float(input("Please Enter The Temprature Into The Fahrenheit Is = "))
print("The Tempreature Into The Fahrnaheit Is = ",str(temp_into_fahrenheit)," Farnheit")
temp_into_centigrade = (temp_into_fahrenheit - 32) * (5 / 9)
print("The Temprature Into The Entigrade Is = ",str(temp_into_centigrade)," Centigrades")
temp_into_kelvin = temp_into_centigrade + 273.15
print("The Temprature Into The Kelvin Is = ",str(temp_into_kelvin)," Kelvin")