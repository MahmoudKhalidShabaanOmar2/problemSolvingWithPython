# write a python program to make dictionary of the author name with book name , and then display the frist author name , and the frist book name from the dictionary of the author name with book name by using different functions methods =>
# dictionary_of_author_name_with_book_name = {}
# def get_dictionary_of_author_name_with_book_name(dict_of_author_name_with_book_name) :
#     for i in range(5) :
#         author_name = input("please enter the name of the author is : ")
#         book_name = input("please enter the name of the book is : ")
#         dict_of_author_name_with_book_name[author_name] = book_name
#     print("the dictionary of the author name with the book name is : "+str(dict_of_author_name_with_book_name))
#     print("the frist author name from the dictionary of the author name with book name is : "+str(list(dict_of_author_name_with_book_name.keys())[0]))
#     print("the frist book name from the dictionary of the author name with book name is : "+str(list(dict_of_author_name_with_book_name.values())[0]))
# get_dictionary_of_author_name_with_book_name(dictionary_of_author_name_with_book_name)
    
def get_dictionary_of_author_name_with_book_name(dict_of_author_name_with_book_name) :
    print("the dictionary of the author name with the book name is : "+str(dict_of_author_name_with_book_name))
    return("the frist author name is : "+str(list(dict_of_author_name_with_book_name.keys())[0])+" , and the frist book name is : "+str(list(dict_of_author_name_with_book_name . values())[0])+" from the dictionary of the author name with book name")    
dictionary_of_author_name_with_book_name = {}
for i in range(5) :
    author_name = input("please enter the author name is : ")
    book_name = input("please enter the book name is : ")
    dictionary_of_author_name_with_book_name[author_name] = book_name 
dict_author_with_book = get_dictionary_of_author_name_with_book_name(dictionary_of_author_name_with_book_name)
print(dict_author_with_book)