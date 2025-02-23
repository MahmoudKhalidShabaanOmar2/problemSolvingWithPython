# write a python program to generate 1 to 10 number with their square , and cube and aslo display their addition of the square , and cube of the number =>
print("generation all numbers from starting number is \"1\" to the ending number is \"10\" is : ")
print("Number\t\tSquareOfNum\tCubeOfNum\tAdditionOfSquareCubeOfNum")
for num in range(1 , 11) :
    # print(str(num)+"\t\t"+str(num * num)+"\t\t"+str(num * num * num)+"\t\t"+str((num * num) + (num * num * num)))
    # print(str(num)+"\t\t"+str(num ** 2)+"\t\t"+str(num ** 3)+"\t\t"+str((num ** 2) + (num ** 3)))
    print(str(num)+"\t\t"+str(pow(num , 2))+"\t\t"+str(pow(num , 3))+"\t\t"+str((pow(num , 2)) + pow(num , 3)))
    # square_of_num = num * num 
    # square_of_num = num ** 2
    square_of_num = pow(num , 2)
    # cube_of_num = num * num * num 
    # cube_of_num = num ** 3
    cube_of_num = pow(num , 3)
    addition_of_square_cube_of_num = square_of_num + cube_of_num 
    # print(str(num)+"\t\t"+str(square_of_num)+"\t\t"+str(cube_of_num)+"\t\t"+str(addition_of_square_cube_of_num))