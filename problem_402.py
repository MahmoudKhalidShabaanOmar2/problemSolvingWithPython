# write a python program to get the temprature into the centigrade , and then converted into kelvin , and fahrenhit by using function method =>
temprature_into_centigrade = float(input("Please Enter The Temprature Into The Centigrade Is = "))
def get_temprature_into_kelvin_fahrenheit(temp_into_centi):
    print("The Temprature Into The Centigrade Is = ",str(temp_into_centi)," Centigrade")
    temprature_into_kelvin = temp_into_centi + 273.15
    print("The Temprature Into Kelvin Is = ",str(temprature_into_kelvin)," Kelvin")
    temprature_into_fahrenheit = (temp_into_centi * 9/5) + 32
    print("The Temprature Into The Fahrenheit Is = ",str(temprature_into_fahrenheit)," Fahrenheit")
get_temprature_into_kelvin_fahrenheit(temprature_into_centigrade)