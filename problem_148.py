# write a python program to generate only even numbers from 1 to 30 by using function method =>
# def generate_only_even_numbers() :
#     print("generating only even numbers from starting number is = \"1\" to the ending number is = \"30\"")
#     for num in range(1 , 31) :
#         if(num %2 == 0):
#             print(num)
# generate_only_even_numbers()

def generate_only_even_numbers() :
    print("generating only even numbers from starting number is = \"0\" to ending number is = \"30\"")
    for num in range(0 , 31 , 2) :
        print(num)
generate_only_even_numbers()