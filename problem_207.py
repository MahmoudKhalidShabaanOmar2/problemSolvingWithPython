# write a python program to make dictionary of author name with book name , and then display the last author name , and last book name from the dictionary of author name with book name by using different functions methods =>
# dictionary_of_author_name_with_book_name = {}
# def get_dictionary_of_author_name_with_book_name(dict_of_author_name_with_book_name) :
#     for i in range(5) :
#         author_name = input("please enter the name of the author is : ")
#         book_name = input("please enter the name of the book is : ")
#         dict_of_author_name_with_book_name[author_name]  = book_name
#     print("the dictionary of the author name with book name is : "+str(dict_of_author_name_with_book_name)) 
#     # print("the last author name from the dictionary of the author name with the book name is : "+str(list(dict_of_author_name_with_book_name . keys())[-1]))
#     print("the last author name from the dictionary of the author name with book name is : "+str(list(dict_of_author_name_with_book_name . keys())[4]))
#     # print("the last book name from the dictionary of the author name with the book name is : "+str(list(dict_of_author_name_with_book_name.values())[-1]))
#     print("the last book name from the dictionary of the author name with the book name is : "+str(list(dict_of_author_name_with_book_name . values())[4]))
# get_dictionary_of_author_name_with_book_name(dictionary_of_author_name_with_book_name)

def get_dictionary_of_author_name_with_book_name(dict_of_author_name_with_book_name) :
    print("the dictionary of the author name is : "+str(dict_of_author_name_with_book_name))
    # return("the last author name is : "+str(list(dict_of_author_name_with_book_name . keys())[4])+" , and the last book name is : "+str(list(dict_of_author_name_with_book_name . values())[4])+" from the dictionary of the author name with the book name")
    return("the last author name is : "+str(list(dictionary_of_author_name_with_book_name . keys())[-1])+" , and the last book name is : "+str(list(dictionary_of_author_name_with_book_name . values())[-1])+" from the dictionary of the author name with the book name")
dictionary_of_author_name_with_book_name = {}
for i in range(5) :
    author_name = input("please enter the name of the book is : ")
    book_name = input("please enter the name of the book is : ")
    dictionary_of_author_name_with_book_name[author_name] = book_name
dict_of_author_with_book = get_dictionary_of_author_name_with_book_name(dictionary_of_author_name_with_book_name)
print(dict_of_author_with_book)