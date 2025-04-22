# write a python program to generate number from 0 to 20 only divisible by 3 number , and generate 0 to 20 only divisible by 5 , and then add both generated number to each other to display the total number => 
# print("Generating All Numbers From Starting Number Is = 0 To The Ending Number Is = 20 That Divisible By Three Is : ")
# sumOfAllNumbersDivBy3= 0 
# for i in range(0 , 21) :
#     if(i %3 == 0) :
#         print(i)
#         sumOfAllNumbersDivBy3 += i
# print("The Sum Of All Numbers That Divisible By Three Is = ",sumOfAllNumbersDivBy3)
# print("Generating All Numbers From Starting Number Is = 0 To The Ending Number Is = 20 That Divisible By Five Is : ")
# sumOfAllNumbersDivBy5 = 0
# for j in range(0 , 21) :
#     if(j %5 == 0) :
#         print(j)
#         sumOfAllNumbersDivBy5 += j 
# print("The Sum Of All Numbers That Divisible By Five Is = ",sumOfAllNumbersDivBy5)
print("Generating All Numbers From Starting Number Is = 0 To The Ending Number Is = 20 That Divisible By Three Is : ")
sumOfAllNumbersDivBy3 = 0
for i in range(0 , 21 , 3) :
    print(i)
    sumOfAllNumbersDivBy3 += i 
print("The Sum Of All Numbers That Divisible By Three Is = ",sumOfAllNumbersDivBy3)
print("Generating All Numbers From Starting Number Is = 0 To The Ending Number Is = 20 That Divisible By Five Is : ")
sumOfAllNumbersDivBy5 = 0 
for j in range(0 , 21 , 5) :
    print(j)
    sumOfAllNumbersDivBy5 += j
print("The Sum Of All Numbers That Divisible By Five Is = ",sumOfAllNumbersDivBy5)