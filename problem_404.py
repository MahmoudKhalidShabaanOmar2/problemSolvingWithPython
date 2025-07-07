# write a python program to get the temprature into the kelvin , and then converted into centigrade , and fahrenheit temprature by using funtion method =>
temprature_into_kelvin = float(input("Please Enter The Temprature Into The Kelvin Is = "))
def get_temprature_into_centigrade_fahrenheit(temp_into_kelvin) :
    print("The Temprature Into The Kelvin Is = ",str(temp_into_kelvin))
    temprature_into_centigrade = temp_into_kelvin + 273.15 
    print("The Temprature Into The Centigrade Is = ",str(temprature_into_centigrade)," Centigrade")
    temprature_into_fahrenheit = (temprature_into_centigrade * 9/5) + 32
    print("The Temprature Into The Fahrenheit Is = ",str(temprature_into_fahrenheit)," Fahrenheit")
get_temprature_into_centigrade_fahrenheit(temprature_into_kelvin)