# write a python program to display only odd numbers from 1 to 30 by using function method =>
# def generating_only_odd_numbers() :
#     print("generating only odd numbers from starting number is = \"1\" to ending number is = \"30\"")
#     for num in range(1 ,31) :
#         if(num %2 != 0) :
#             print(num)
# generating_only_odd_numbers()

def generating_only_odd_numbers() :
    print("generating only odd numbers from starting number is = \"1\" to ending number is = \"30\"")
    for num in range(1 , 31 , 2) :
        print(num)
generating_only_odd_numbers()