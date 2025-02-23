# write a python program to generate numbers from 1 to 10 and get square of number , and cube of number , and also display the result of the addition of square , and cube of number by using function methods =>
def generating_numbers_from_1_to_10_get_square_cube_of_num() :
    print("generation all numbers from starting number is \"1\" to ending number is \"10\" is : ")
    print("Number\t\tSquareOfNumber\tCubeOfNumber\tAdditionOfSquareCubeOfNumber")
    for num in range(1 , 11) :
        # print(str(num)+"\t\t"+str(num * num)+"\t\t"+str(num * num * num)+"\t\t"+str((num * num) + (num * num * num)))
        # print(str(num)+"\t\t"+str(num ** 2)+"\t\t"+str(num * num * num)+"\t\t"+str((num ** 2) + (num ** 3)))
        # print(str(num)+"\t\t"+str(pow(num , 2))+"\t\t"+str(pow(num , 3))+"\t\t"+str((pow(num , 2)) + (pow(num , 3))))
        # square_of_num = num * num 
        # square_of_num = num ** 2
        square_of_num = pow(num , 2)
        # cube_of_num = num * num * num 
        # cube_of_num = num ** 3
        cube_of_num = pow(num , 3)
        addition_of_square_cube_of_number = square_of_num + cube_of_num 
        print(str(num)+"\t\t"+str(square_of_num)+"\t\t"+str(cube_of_num)+"\t\t"+str(addition_of_square_cube_of_number))
generating_numbers_from_1_to_10_get_square_cube_of_num()
