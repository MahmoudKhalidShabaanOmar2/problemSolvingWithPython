# write a python program to get data items from the user , how much integer , float , boolean , And string type of data is stored in a list By Using Static List Of Different Elements =>
lista_of_different_elements = ["Mahmoud Khalid" , "22 Years Old" , "Computer Science , And Information System" , "Six October University" , "-123" , "123" , "234.234" , "-2345.345" , True , False , 123 , -234 , 234.3456 , -234.234]
print("The List Of Different Elements Is : "+str(lista_of_different_elements)+" Elements")
print("The Length Of The List Of Different Elements Is = "+str(len(lista_of_different_elements))+" Elements")
integerDataType = 0 
floatDataType = 0 
booleanDataType = 0 
stringDataType = 0 
for dataType in lista_of_different_elements :
    print("The Data Item Is : "+str(dataType)+" , And The Type Of The Data Item Is : "+str(type(dataType)))
    if(type(dataType) == int) :
        integerDataType += 1
    if(type(dataType) == float) :
        floatDataType += 1 
    if(type(dataType) == bool) :
        booleanDataType += 1 
    if(type(dataType) == str) :
        stringDataType += 1
print("The Number Of The Data Items With Integer Data Type Is = "+str(integerDataType)+" Integer Data Types")
print("The Number Of The Data Items With Float Data Type Is = "+str(floatDataType)+" Float Data Types")
print("The Number Of The Data Items With Boolean Data Type Is = "+str(booleanDataType)+" Boolean Data Types")
print("The Number Of The Data Items With String Data Type Is = ",str(stringDataType)+" String Data Types")