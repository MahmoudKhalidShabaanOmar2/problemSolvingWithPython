# write a python program to create nested tuple by using function =>
nested_lista = [1 , 2 , [2 , 4 , 5 , 7] , [True , False] , "ahmed" , ["ahmed" , "false" , "true"] , 2.45 , 232,343 , -434 , -34343 , [32.434 , 3434.45645 , -4556.6767]]
def get_nested_tuple(nested_list):
    print("The Nested List Is ",str(nested_list))
    converted_list = [] 
    for i in nested_list:
        if(isinstance(i , list)):
            converted_list.append(tuple(i))
        else:
            converted_list.append(i)
    nested_tuple = tuple(converted_list)
    print("The Nested Tuple Is : ",str(nested_tuple))
get_nested_tuple(nested_lista)