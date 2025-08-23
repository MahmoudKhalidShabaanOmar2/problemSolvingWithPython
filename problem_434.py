# write a python program to get the temprature into the fahrenheit , and then converted temprature into kelvin , and centigrade by using function method =>
temprature_into_fahrenheit = int(input("Please Enter The Temprature Into The Fahrenheit Is = "))
def get_temprature_into_kelvin_centigrade(temp_into_fahren):
    print("The Temprature Into The Fahrenheit Is = ",str(temp_into_fahren)," Fahrenheit")
    temprature_into_centigrade = (temp_into_fahren - 32) * 5/9
    print("The Temprature Into The Centigrade Is = ",str(temprature_into_centigrade)," Centigrade")
    temprature_into_kelvin = (temp_into_fahren - 32) * 5/9 + 273.15
    print("The Temprature Into The Kelvin Is = ",str(temprature_into_kelvin)," Kelvin")
get_temprature_into_kelvin_centigrade(temprature_into_fahrenheit)