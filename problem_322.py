# write a python program to get data items from the user , how much integer , float , and string type of data is stored in a list By Using Static List Of Different Elements =>
lista_of_different_elements = ["Mahmoud Khalid" , 2341 , "22 Years Old" , -234345 , "Computer Science , And Information System" , 234345.234345 , "Six October University" , -3454.3456 , "23423" , "2345.4567" , "-23456" , "-3456.345"]
print("The List Of Different Elements Is : "+str(lista_of_different_elements))
print("The Length Of The List Of Different Elements Is = "+str(len(lista_of_different_elements))+" Elements")
integerDataType = 0
stringDataType = 0 
floatDataType = 0
for dataType in lista_of_different_elements :
    if(type(dataType) == str) :
        stringDataType += 1
    print("The Number Of Data Items With String Data Type Is = ",str(stringDataType)+" String Data Types")
    if(type(dataType) == int) :
        integerDataType += 1 
    print("The Number Of Data Items With Integer Data Type Is = "+str(integerDataType)+" Integer Data Types")
    if(type(dataType == float)) :
        floatDataType += 1 
    print("The Number Of Data Items With Float Data Type Is = "+str(floatDataType)+" Float Data Types")