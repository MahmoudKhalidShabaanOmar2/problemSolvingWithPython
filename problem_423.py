# write a python program to access different items from the nested list =>
nested_list = [1 , 2 , 3 , ["mahmoud" , "khalid"] , [True , False] , [-23 , -24 , -343] , [-242.2424 , -3546.46464]]
print("The Nested List Is : ",str(nested_list))
for list in nested_list:
    print(list)
print("The Access Item From A Nested List Is : ",str(nested_list[3][1]))