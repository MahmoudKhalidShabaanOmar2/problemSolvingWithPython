# write a python program to get five author name with book name , and then display last author with it's book name =>
dictionary_of_author_name_with_book_name = {}
for i in range(5) :
    author_name = input("please enter the author name is : ")
    book_name = input("please enter the name of the book is : ")
    dictionary_of_author_name_with_book_name[author_name] = book_name
print("the dictionary of the author name with book name is : "+str(dictionary_of_author_name_with_book_name))
# print("the last author name from the dictionary of the author name with book name is : "+str(list(dictionary_of_author_name_with_book_name . keys())[-1]))
print("the last author name from the dictionary of the author name with book name is : "+str(list(dictionary_of_author_name_with_book_name . keys())[4]))
# print("the last book name from the dictionary of the author name with book name is : "+str(list(dictionary_of_author_name_with_book_name . values())[-1]))
print("the last book name from the dictionary of the author name with book name is : "+str(list(dictionary_of_author_name_with_book_name . values())[4]))