# write a python program to get list of different data items from the user , and then how many integer , float , string , boolean data types in the list of the different data items by using function method =>
lista_of_different_data_items = ["Mahmoud Khalid Shabaan Omar" , "22 Years" , "Six October University" , "Computer Science , And Information System" , "Male" , "12123" , "-12356" , "2345.345678" , "-4567.56789" , 234567 , -34567 , 34567.5678 , -456789.5678 , True , False , "True" , "False"]
def get_lista_of_different_data_items(list_of_data_items) : 
    print("The List Of Different Data Items : ",str(list_of_data_items))
    print("The Length Of The List Of Different Data Items Is = ",str(len(list_of_data_items))+" Data Items")
    integerDataType = 0
    floatDataType = 0 
    booleanDataType = 0 
    stringDataType = 0
    for dataType in list_of_data_items : 
        print("The Data Item Is : ",str(dataType)," , And The Type Of The Data Item Is : ",str(type(dataType)))
        if(type(integerDataType) == int) :
            integerDataType += 1 
        if(type(floatDataType) == float) :
            floatDataType += 1 
        if(type(booleanDataType) == bool) : 
            booleanDataType += 1
        if(type(stringDataType) == str) : 
            stringDataType += 1 
        
    print("The Total Length Of The Integer Data Type Is = ",str(integerDataType)," IntegerDataTypes")        
    print("The Total Length Of The Float Data Types Is = ",str(floatDataType)," FloatDataTypes")
    print("The Total Length Of The Boolean Data Types Is = ",str(booleanDataType)," BooleanDataTypes")
    print("The Total Length Of The String Data Types Is = ",str(stringDataType)," StringDataTypes")
get_lista_of_different_data_items(lista_of_different_data_items)