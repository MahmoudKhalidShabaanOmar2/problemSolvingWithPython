# write a python program to create a list to pass to function as parameter to display it's elements in the reverse order =>
# # lista_of_different_elements = []
# # for i in range(10) :
# #     elements = input("please enter the different elements to store in the list of the different elements is : ")
# #     lista_of_different_elements . append(elements)
# lista_of_different_elements = [input("please enter the different elements to store in the list of the different elements is : ") for i in range(5)]
# def get_lista_of_different_elements(list_of_ele) :
#     print("the list of the different elements is : "+str(list_of_ele))
#     for i in list_of_ele :
#         print(i)
#     list_of_ele . reverse()
#     print("the reversing (descending) sequence of the list of the different elements is : "+str(list_of_ele))
#     for j in list_of_ele :
#         print(j)
# get_lista_of_different_elements(lista_of_different_elements)

def get_list_of_different_elements(list_of_ele) :
    print("the list of the different elements is : "+str(list_of_ele))
    for i in list_of_ele : 
        print(i)
    list_of_ele.reverse()
    print("the reversing (descending) sequence of the list of the different elements is : "+str(list_of_ele))
    for j in list_of_ele :
        print(j)
    return("")
lista_of_different_elements = []
for k in range(5) :
    elements = input("please enter the different elements to store in the list of the different elements is : ")
    lista_of_different_elements . append(elements)
list_of_dif_ele = get_list_of_different_elements(lista_of_different_elements)
print(list_of_dif_ele)
