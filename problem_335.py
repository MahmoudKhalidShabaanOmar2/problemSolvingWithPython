# write a python program to get lowercase words to store in the list => 
lista_of_lower_words = []
for i in range(10) :
    word = input(f"Please Enter The Word {i + 1} Is : ")
    if(word.islower()) :
        lista_of_lower_words.append(word)
        print("The List Of The Lowercase(small) Words Only Is : "+str(lista_of_lower_words))
    else :
        print("Error , Please Enter Only Lowercase (Small) Words")
print("The List Of The Lowercase (Smaller) Words Is : ",str(lista_of_lower_words))