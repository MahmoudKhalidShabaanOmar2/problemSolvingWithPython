# write a python program to get total numbers from a nested list =>
nested_lista = [1 , 2 , 3 , [4 , 5 , 6] , "mahmoud" , "khalid" , [2.5 , -5 , -5.4] , True , False , ["amhmoud Khalid" , "23 Years Old" , "Computer Science , And Information System"]]
print("The Nested List Of All Elements Is : ",str(nested_lista))
total_numbers_in_nested_lista = 0
for i in nested_lista: 
    if(type(i) == list):
        total_numbers_in_nested_lista += 1
print("The Sum Of All Numbers In Nested List Is = ",str(total_numbers_in_nested_lista))