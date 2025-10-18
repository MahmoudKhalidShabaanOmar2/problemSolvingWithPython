# write a java script to access multiple elements from the list by using function method =>
lista = [12 , 434 , 35 , 565.67644 , 34.455 , -34343 , -6565 , -3434.45645 , -4545.454 , "Mahmoud Khalid" , "Male" , True , False , "true" , "false"]
def access_multiple_elements_from_list(lst):
    print("The List Is : ",str(lst))
    starting_position = int(input("Please Enter The Starting Position Is = "))
    print("The Starting Position Is = ",str(starting_position))
    ending_position = int(input("Please Enter Ending Position Is = "))
    print("The Ending Position Is = ",str(ending_position))
    multiple_elements_from_list = lst[starting_position:ending_position+1]
    print("The Multiple Elements From The List Is : ",str(multiple_elements_from_list))
access_multiple_elements_from_list(lista)