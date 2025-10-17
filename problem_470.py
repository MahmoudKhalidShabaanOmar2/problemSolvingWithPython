# write a python program to access different nested list from the nested list of different elements =>
nested_lista = [1 , 2 , [2 , 4 , 5 , 7] , [True , False] , "ahmed" , ["ahmed" , "false" , "true"] , 2.45 , 232,343 , -434 , -34343 , [32.434 , 3434.45645 , -4556.6767]]
print("The Nested List Is : ",str(nested_lista))
print("The Nested List From The Parent Nested List Is : ",str(nested_lista[2]))
print("The Element From The Nested List From The Parent Nested List Is = ",str(nested_lista[2][3]))