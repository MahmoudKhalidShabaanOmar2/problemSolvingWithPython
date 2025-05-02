# write a python program to get only uppercase words to store in the list =>
lista_of_upper_words = []
for i in range(10) :
    word = input(f"Please Enter The Word Is : ")
    if(word.isupper()) :
        lista_of_upper_words . append(word)
        print("The List Of The Uppercase Words Is : ",str(lista_of_upper_words))
    else :
        print("Error , Please Enter Uppercase Words")