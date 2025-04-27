# write a python program to get data items from the user , and then how much integer , float , string , and at the end boolean data types , and you should know that other data items are stored in a static list of different elements by using function methods =>
lista_of_different_elements = ["Mahmoud Khalid Shabaan Omar" , "Male" , "22 Years Old" , "Computer Science , And Information System" , "Six October University" , "231" , "-3453" , "3434.2323" , "-23232.43434" , 123 , -234 , 32323.323 , -223232.43434 , True , False]
def get_lista_of_different_elements(list_of_diff_ele) :
    print("The List Of Different Elements Is : "+str(list_of_diff_ele))
    print("The Length Of The List Of Different Elements Is = "+str(len(list_of_diff_ele))+" Elements")
    integerDataType = 0
    floatDataType = 0 
    stringDataType = 0 
    booleanDataType = 0 
    for dataType in lista_of_different_elements :
        print("The Data Item Is : "+str(dataType)+" , And The Data Type Of The Data Item Is : "+str(type(dataType)))
        if(type(dataType) == int) :
            integerDataType += 1
        if(type(dataType) == float) :
            floatDataType += 1 
        if(type(dataType) == str) :
            stringDataType += 1
        if(type(dataType) == bool) :
            booleanDataType += 1
    print("The Number Of The Data Items With The Integer Data Type Is = "+str(integerDataType)+" Integer Data Types")
    print("The Number Of The Data Items With The Boolean Data Type Is = ",str(booleanDataType)+" Boolean Data Types")
    print("The Number Of The Data Items With The String Data Type Is = ",str(stringDataType)," String Data Types")
    print("The Number Of The Data Items With The Float Data Type Is = ",str(floatDataType)," Float Data Types")
get_lista_of_different_elements(lista_of_different_elements)