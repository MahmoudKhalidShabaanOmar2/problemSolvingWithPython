# write a python program to get area , and parameter of the square by using different functions methods =>
# length_of_square = int(input("please enter the length of the square is = "))
# def get_area_parameter_of_square(len_of_sqr) :
#     print("the length of the square is = "+str(len_of_sqr))
#     # area_of_square = len_of_sqr * len_of_sqr 
#     # area_of_square = pow(len_of_sqr , 2)
#     area_of_square = len_of_sqr ** 2
#     print("the area of the square is = "+str(area_of_square))
#     parameter_of_square = 4 * len_of_sqr 
#     print("the parameter of the square is = "+str(parameter_of_square))
# get_area_parameter_of_square(length_of_square)
    
# length_of_square = int(input("please enter the length of the square is = "))
# def get_area_parameter_of_square(len_of_sqr) :
#     print("the length of the square is = "+str(len_of_sqr))
#     if(len_of_sqr > 0) :
#         area_of_square = len_of_sqr * len_of_sqr 
#         print("the area of the sqare is = "+str(area_of_square))
#         parameter_of_square = 4 * len_of_sqr 
#         print("the parameter of the square is = "+str(parameter_of_square))
#     else :
#         print("please enter a valid length of the square")
# get_area_parameter_of_square(length_of_square)

# def get_area_parameter_of_square(len_of_sqr) :
#     print("the length of the square is = "+str(len_of_sqr))
#     if(len_of_sqr > 0) :
#         # area_of_square = len_of_sqr * len_of_sqr 
#         # area_of_square = pow(len_of_sqr , 2)
#         area_of_square = len_of_sqr ** 2 
#         parameter_of_square = 4 * len_of_sqr 
#         return("the area of the square is = "+str(area_of_square)+" , and the parameter of the square is = "+str(parameter_of_square))
#     else :
#         return("please enter valid length of the square")
# length_of_square = int(input("please enter the length of the square is = "))
# area_parameter = get_area_parameter_of_square(length_of_square)
# print(area_parameter)

def get_area_parameter_of_square(len_of_sqr) :
    print("the length of the square is = "+str(len_of_sqr))
    # area_of_square = len_of_sqr * len_of_sqr 
    # area_of_square = pow(len_of_sqr , 2)
    area_of_square = len_of_sqr ** 2
    parameter_of_square = len_of_sqr * 4 
    return("the area of the square is = "+str(area_of_square)+" , and the parameter of the square is = "+str(parameter_of_square))
length_of_square = int(input("please enter the length of the square is = "))
area_parameter_of_sqr = get_area_parameter_of_square(length_of_square)
print(area_parameter_of_sqr)