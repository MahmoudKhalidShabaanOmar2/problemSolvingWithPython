# write a python program to make dictionary of the author name with book name , and then display the frist author name , and frist book name from the dictionary of the author name with book name =>
dictionary_of_author_name_with_book_name = {}
for i in range(5) :
    author_name = input("please enter the author name is : ")
    book_name = input("please enter the book name is : ")
    dictionary_of_author_name_with_book_name[author_name] = book_name 
print("the dictionary of the author name with book name is : "+str(dictionary_of_author_name_with_book_name))
print("the author name from the dictionary of the author name with book name is : "+str(list(dictionary_of_author_name_with_book_name . keys())[0]))
print("the book name from the dictionary of the author name with book name is : "+str(list(dictionary_of_author_name_with_book_name . values())[0]))