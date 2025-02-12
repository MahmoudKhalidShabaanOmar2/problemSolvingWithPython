# write a python program to get the intersection between the three sets =>
frist_set = {5 , 2 , 4 , 6 , 7 , 1}
second_set = {5 , 3 , 11}
third_set = {4 , 5 , 12 , 2 , 1 , 0}
print("the different values of the different sets is : \n")
print("the frist set is : "+str(frist_set))
print("the second set is : "+str(second_set))
print("the third set is : "+str(third_set))
intersection_set = frist_set . intersection(second_set , third_set)
print("the intersection between the three sets is : "+str(intersection_set))