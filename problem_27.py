# write a python program to get the symmetric difference between the two sets =>
frist_set = {1 , 2 , 6 , 7 , 8 , 12}
second_set = {1 , 6 , 0 , 15 , 3}
print("the different values of the different set is : ")
print("the frist set is : "+str(frist_set))
print("the second set is : "+str(second_set))
symmetric_difference_set = frist_set . symmetric_difference(second_set)
print("the symmetric difference between the two sets is : "+str(symmetric_difference_set))