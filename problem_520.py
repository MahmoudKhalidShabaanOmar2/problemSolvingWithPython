# write a python program to create one dimenssional array by using arange built in function by using function method =>
import numpy as np 
def creating_one_dimenssional_array(one_dimenssional_arr):
    print("The One Dimenssional Array Is : ")
    return one_dimenssional_arr 
one_dimenssional_array = np.arange(1 , 11)
displaying_one_dimenssional_array = creating_one_dimenssional_array(one_dimenssional_array)
print(displaying_one_dimenssional_array)