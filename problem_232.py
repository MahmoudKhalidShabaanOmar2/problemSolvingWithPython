# write a python program to get six different elements in list , and then clear all elements from the list , and then check if list is empty list or not empty list by using different function methods =>
# def isEmptyLista(lista) :
#     return not lista 
# # lista_of_different_elements = []
# # for i in range(6) :
# #     lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
# lista_of_different_elements = [input("please enter the different elements to store in the list of the different elements is : ") for i in range(6)]
# def isEmpty(list_of_diff_elem) :
#     print("the list of the different elements before clearing all elements from the list of the different elements is : "+str(list_of_diff_elem)) 
#     list_of_diff_elem . clear()
#     print("the list of the different elements after clearing all elements from the list of the different elements is : "+str(list_of_diff_elem)) 
#     if(isEmptyLista(list_of_diff_elem)) :
#         print("it is empty list")
#     else :
#         print("it is not empty list")
# isEmpty(lista_of_different_elements)

# def isEmptyLista(lista) :
#     return not lista 
# def isEmpty(list_of_diff_elem) :
#     print("the list of the different elements before clearing all elements from the list of the different elements is : "+str(list_of_diff_elem))
#     list_of_diff_elem . clear() 
#     print("the list of the different elements after clearing all elements from the list of the different elements is : "+str(list_of_diff_elem)) 
#     if(isEmptyLista(list_of_diff_elem)) :
#         return("it is empty list")
#     else :
#         return("it is not empty list")
# # lista_of_different_elements = []
# # for i in range(6) :
# #     lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
# lista_of_different_elements = [input("please enter the different elements to store in the list of the different elements is : ") for i in range(6)]
# empty = isEmpty(lista_of_different_elements)
# print(empty)

# def isEmptyLista(lista) :
#     return len(lista) == 0
# # lista_of_different_elements = []
# # for i in range(6) :
# #     lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
# lista_of_different_elements = [input("please enter the different elements to store on the list of the different elements is : ") for i in range(6)]
# def isEmpty(list_of_diff_elem) :
#     print("the list of the different elements before clearing all elements from the list of the different elements is : "+str(list_of_diff_elem))
#     list_of_diff_elem . clear()
#     print("the list of the different elements after clearing all elements from the list of the different elements is : "+str(list_of_diff_elem)) 
#     if(isEmptyLista(list_of_diff_elem)) :
#         print("it is empty list")
#     else :
#         print("it is not empty list")
# isEmpty(lista_of_different_elements)

# def isEmptyLista(lista) :
#     return len(lista) == 0
# def isEmpty(list_of_diff_elem) :
#     print("the list of the different elements before cleaing all different elements from the list of the different elements is : "+str(list_of_diff_elem))
#     list_of_diff_elem . clear() 
#     print("the list of the different elements after clearing all different elements from the list of the different elements is : "+str(list_of_diff_elem))
#     if(isEmptyLista(list_of_diff_elem)) :
#         return("it is empty list")
#     else :
#         return("it is not empty list")
# # lista_of_different_elements = []
# # for i in range(6) :
# #     lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
# lista_of_different_elements = [input("please enter the different elements to store in the list of the different elements is : ") for i in range(6)]
# empty = isEmpty(lista_of_different_elements)
# print(empty)

# # lista_of_different_elements = []
# # for i in range(6) :
# #     lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : ")) 
# lista_of_different_elements = [input("please enter the different elements to store different elements in the list of the different elements is : ") for i in range(6)]
# def isEmptyLista(list_of_diff_elem) :
#     print("the list of the different elements before clearing all elements from the list of the different elements is : "+str(list_of_diff_elem))
#     list_of_diff_elem . clear()
#     print("the list of the different elements before removing all elements from the list of the different elements is : "+str(list_of_diff_elem))
#     if(not list_of_diff_elem) :
#         print("it is empty list")
#     else :
#         print("it is not empty list")
# isEmptyLista(lista_of_different_elements)

lista_of_differen_elements = []
def isEmptyLista(list_of_diff_elem) :
    print("the list of the different elements before clearing all different elements from the list of the different elements is "+str(list_of_diff_elem))
    list_of_diff_elem . clear()
    print("the list of the different elements after clearing all different elements from the list of the different elements is : "+str(list_of_diff_elem))
    if(not list_of_diff_elem) :
        return("it is empty list")
    else :
        return("it is not empty list")
lista_of_different_elements = []
for i in range(6) :
    lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
emptyLista = isEmptyLista(lista_of_different_elements)
print(emptyLista)