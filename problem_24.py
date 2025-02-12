# write a python program to make the intersection between the three sets by using function methods =>
# frist_set = {5 , 2 , 4 , 6 , 7 , 1}
# second_set = {5 , 3 , 11}
# third_set = {4 , 5 , 12 , 2 , 1 , 0}
# def get_intersection_set(fri_set , sec_set , thi_set) :
#     print("the different values of the different sets is : \n")
#     print("the frist set is : "+str(fri_set))
#     print("the second set is : "+str(sec_set))
#     print("the third set is : "+str(thi_set))
#     intersection_set = fri_set . intersection(sec_set , thi_set)
#     print("the intersection between the three sets is : "+str(intersection_set))
# get_intersection_set(frist_set , second_set , third_set)

def get_intersection_set(fri_set , sec_set , thi_set) :
    print("the different values of the different sets is : \n")
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    print("the third set is : "+str(thi_set))
    intersection_set = fri_set . intersection(sec_set , thi_set)
    return("the intersection between the three sets is : "+str(intersection_set))
frist_set = {5 , 2 , 4 , 6 , 7 , 1}
second_set = {5 , 3 , 11}
third_set = {4 , 5 , 12 , 2 , 1 , 0}
interSection = get_intersection_set(frist_set , second_set , third_set)
print(interSection)