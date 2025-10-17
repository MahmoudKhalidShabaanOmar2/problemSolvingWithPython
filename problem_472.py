# write a python program to create a nested tuple =>
nested_lista = [1 , 2 , [2 , 4 , 5 , 7] , [True , False] , "ahmed" , ["ahmed" , "false" , "true"] , 2.45 , 232,343 , -434 , -34343 , [32.434 , 3434.45645 , -4556.6767]]
print("The Nested List Is : ",str(nested_lista))
converted_lista = []
for i in nested_lista:
    if isinstance(i , list):
        print("Converted List Into Tuple.")
        converted_lista.append(tuple(i))
    else:
        print("Not Converted")
        converted_lista.append(i)
nested_tuple = tuple(converted_lista)
print("The Nested Tuple Is : ",str(nested_tuple))