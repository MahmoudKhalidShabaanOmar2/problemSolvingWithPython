# write a python program to get different elements , and then store them in the list , and count the elements from the list , and then display result for the user by using different functions methods =>
# lista_of_different_elements = ["mahmoud khalid shabaan omar awad sallam" , "21 years" , "8 Nassar Nassif Street Kafr El Gabal El Haram El Giza Egypt" , "computer sceience , and information system" , "six october university"]
# def get_list_of_different_elements_count_elements(list_of_elements) :
#     print("the list of the different elements is : "+str(list_of_elements))
#     print("the length of the list of the different elements is = "+str(len(list_of_elements))+" elements")
# get_list_of_different_elements_count_elements(lista_of_different_elements)

def get_list_of_different_elements_count_elements(list_of_elements) :
    print("the list of the different elements is : "+str(list_of_elements))
    return("the length of the list of the different elements is = "+str(len(list_of_elements))+" elements")
lista_of_different_elements = ["mahmoud khalid shabaan omar awad sallam" , "21 years" , "8 Nassar Nassif Street Kafr El Gabal El Haram El Giza Egypt" , "computer sceience , and information system" , "six october university"]
list_of_elements = get_list_of_different_elements_count_elements(lista_of_different_elements)
print(list_of_elements)