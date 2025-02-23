# write a python program to generate all numbers from starting number is = 1 to ending number is = 10 with having four steps difference , and then get square of the number , and cube of the number , and then get the addition of the square of the number , and cube of the number by using function method =>
def generating_all_numbers_from_1_to_10_with_4_steps_differences() :
    print("generating all numbers from starting number is = \"10\" to ending number is = \"1\" with having \"4 steps\" differences is : ")
    print("Number\t\tSquareOfNumber\tCubeOfNumber\tAdditionOfSquareAndCubeOfNumber")
    for num in range(10 , 1 , -4) :
        # print(str(num)+"\t\t"+str(num * num)+"\t\t"+str(num * num * num)+"\t\t"+str((num * num) + (num * num * num)))
        # print(str(num)+"\t\t"+str(num ** 2)+"\t\t"+str(num ** 3)+"\t\t"+str((num ** 2) + (num ** 3)))
        # print(str(num)+"\t\t"+str(pow(num , 2))+"\t\t"+str(pow(num , 2))+"\t\t"+str((pow(num , 2)) + (pow(num , 3))))
        # square_of_num = num * num 
        # square_of_num = num ** 2
        square_of_num = pow(num , 2)
        # cube_of_num = num * num * num 
        # cube_of_num = num ** 3
        cube_of_num = pow(num , 3)
        addition_of_square_of_num_and_cube_of_num = square_of_num + cube_of_num 
        print(str(num)+"\t\t"+str(square_of_num)+"\t\t"+str(cube_of_num)+"\t\t"+str(addition_of_square_of_num_and_cube_of_num))
generating_all_numbers_from_1_to_10_with_4_steps_differences()