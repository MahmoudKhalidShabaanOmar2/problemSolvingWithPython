# write a python program to get the total numbers of list inside nested list by using function method =>
nested_lista = [1 , 2 , 3 , [4 , 5 , 6] , "mahmoud" , "khalid" , [2.5 , -5 , -5.4] , True , False , ["amhmoud Khalid" , "23 Years Old" , "Computer Science , And Information System"] , ["False" , "true" , True , False]]
def countTotalNumbersOfListInsideNestedLista(nestedList):
    print("The Nested List Of All Elements Is : ",str(nestedList))
    total_numbers_of_list_inside_nested_list = 0
    for i in nestedList:
        if(type(i) == list):
            total_numbers_of_list_inside_nested_list += 1
    print("The Total Numbers Of Nested List Inside The Nested List Is = ",str(total_numbers_of_list_inside_nested_list)+" Lists")
countTotalNumbersOfListInsideNestedLista(nested_lista)