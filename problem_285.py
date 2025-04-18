# write a python program to append those number thatv are divisible by 5 , and 7 from a range (10 , 100) to a new created list => 
lista_of_numbers = []
for num in range(10 , 100) :
    if((num %5 == 0) and (num %7 == 0)) :
        lista_of_numbers . append(num)
print("The List Of The Numbers That Divisble By Five , And Seven At The Same Time Is : "+str(lista_of_numbers))