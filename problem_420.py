# write a python program to get a word that contains both upper , and lower characters , and then converted upper to lower character , and lower to upper character =>
import re
word = input("Please Enter The Word Is : ")
print("The Word Is : \""+word+"\"")
pattern = re.search('[a-z]+[A-Z]+' , word)
lista_of_new_char=[]
if pattern:
    for i in word:
        if(i.isupper()):
            newChar = i.lower()
            lista_of_new_char.append(newChar)
        if(i.islower()):
            newChar = i.upper()
            lista_of_new_char.append(newChar)
print("The List Of The New Char Is : ",str(lista_of_new_char))