# write a pyton program to get the temprature into the fahrenheit , and then converted into centigrade , and kelvin by using function method =>
temprature_into_fahrenheit = float(input("Please Enter The Temrature Into The Fahrenheit Is = "))
def get_temprature_into_centigrade_kelvin(temp_into_fahren):
    print("The Temprature Into The Fahrenheit Is = ",str(temp_into_fahren)," Fahrenheit")
    temp_into_centigrade = (temp_into_fahren - 32) * (5 / 9)
    print("The Temprature Into The Centigrade Is = ",str(temp_into_centigrade)," Centigrade")
    temp_into_kelvin = temp_into_centigrade + 273.15 
    print("The Temprature Into The Kelvin Is = ",str(temp_into_kelvin)," Kelvin")
get_temprature_into_centigrade_kelvin(temprature_into_fahrenheit)