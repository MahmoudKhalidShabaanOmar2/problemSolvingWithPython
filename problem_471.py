# write a python program To Access Different Elements From the nested list by using function method =>
nested_lista = [1 , 2 , [2 , 4 , 5 , 7] , [True , False] , "ahmed" , ["ahmed" , "false" , "true"] , 2.45 , 232,343 , -434 , -34343 , [32.434 , 3434.45645 , -4556.6767]]
def access_different_nested_list(nested_list):
    print("The Nested List Is : ",str(nested_list))
    print("The Nested List From The Nested List Is : ",str(nested_list[3]))
    print("The Last Element From The Children Nested List From The Parent Nested List Is : ",str(nested_list[3][1]))
access_different_nested_list(nested_lista)