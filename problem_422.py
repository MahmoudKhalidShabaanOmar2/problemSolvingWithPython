# write a python program to count a total numbers in the nested list of numbers =>
nested_lista = [1 , 2 , 3 , 4 , "ahmed" , "mahmoud" , [1 , 2 , 4 , 6 , "Ahmed" , "Mahmoud"] , [3.5 , 34.34 , 56.867] , [-2424 , -224 , -646] , [-43.353 , -3553.564 , -46.5775]]
print("The Nested List Of Different Lists Is : ",str(nested_lista))
total_numbers_of_lists = 0 
for lista in nested_lista:
    if(type(lista) == list):
        total_numbers_of_lists += 1
print("The Total Numbers Of The Lists In The Nested List Is = ",str(total_numbers_of_lists)+" Lists")