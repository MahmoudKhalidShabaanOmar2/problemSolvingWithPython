# write python program to get five year numbers from the user to store in array , and display only leap year =>
import array as arr 
array_of_year_numbers = arr . array("i" , [])
for i in range(5) :
    array_of_year_numbers . append(int(input("please enter the year number is : ")))
print("the all numbers of the years is : ")
for j in range(5) :
    print(array_of_year_numbers[j])
print("the leap year number only is : ")
for k in range(5) :
    if(array_of_year_numbers[k] %4 == 0) :
        print(array_of_year_numbers[k])