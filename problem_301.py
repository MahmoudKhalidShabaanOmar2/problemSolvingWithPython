# write a python program to generate numbers from 0 to 20 only even numbers , and generate 0 to 20 odd numbers , add both generated number to each other to display total result =>
# print("Generating , Or Displaying Only Even Numbers From The Starting Number Is = 0 To The Ending Number Is = 20 Is : ")
# sum_of_all_even_numbers = 0 
# for i in range(0 , 21 , 2) :
#     print(i)
#     sum_of_all_even_numbers += i 
# print("The Sum Of All Even Number From The Starting Number Is = 0 To The Ending Number Is = 20 Is = ",str(sum_of_all_even_numbers))
# print("\nGenerating , Or Displaying Only Even Numbers From The Starting Number Is = 0 To The Ending Number Is = 20 Is : ")
# sum_of_all_odd_numbers = 0
# for j in range(1 , 21 , 2) :
#     print(j)
#     sum_of_all_odd_numbers += j 
# print("The Sum Of All Odd Numbers From The Starting Number Is = 0 To The Ending Number Is = 20 Is = "+str(sum_of_all_odd_numbers))

print("Generating , Or Displaying Only Even Numbers From The Starting Number Is = 0 To The Ending Number Is = 20 Is : ")
sum_of_all_even_numbers = 0 
for i in range(0 , 21) :
    if(i %2 == 0) :
        print(i)
        sum_of_all_even_numbers += i 
print("The Sum Of All Even Numbers From The Starting Number Is = 0 To The Ending Number Is = 20 Is = "+str(sum_of_all_even_numbers))
print("Generating , Or Displaying Only Odd Numbers From The Starting Number Is = 0 To The Ending Number Is = 20 Is : ")
sum_of_all_odd_numbers = 0
for j in range(0 , 21) :
    if(j %2 != 0) :
        print(j)
        sum_of_all_odd_numbers += j 
print("The Sum Of All Odd Numbers From Starting Number Is = 0 To The Ending Number Is = 20 Is = ",str(sum_of_all_odd_numbers))