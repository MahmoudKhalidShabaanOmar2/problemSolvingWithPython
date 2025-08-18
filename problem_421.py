# write a python program to get number from the user , and then display number from zero to the entered number =>
inputNumber = int(input("Please Enter The Number Is = "))
print("The Input Number Is = ",str(inputNumber))
print("All Numbers From Zero To Your Entered Number Is : ")
for num in range(0 , inputNumber+1):
    print(num)