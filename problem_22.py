# write a python program to get the intersection of the two sets by using function method =>
# frist_set = {5 , 2 , 4 , 6 , 7 , 1}
# second_set = {5 , 3 , 11}
# def get_intersection_set(fri_set , sec_set) :
#     print("the different values of the different set is : \n")
#     print("the frist set is : "+str(fri_set))
#     print("the second set is : "+str(sec_set))
#     intersection_set = fri_set . intersection(sec_set)
#     print("the intersection set between the two sets is : "+str(intersection_set))
# get_intersection_set(frist_set , second_set)


def get_intersection_set(fri_set , sec_set) :
    print("the different values of the different sets is : \n")
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    intersection_set = fri_set . intersection(sec_set)
    return("the intersection set between the two sets is : "+str(intersection_set))
frist_set = {5 , 2 , 4 , 6 , 7 , 1}
second_set = {5 , 3 , 11}
interSection = get_intersection_set(frist_set , second_set)
print(interSection)
