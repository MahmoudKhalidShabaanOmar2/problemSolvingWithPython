# write a python program to get memory into giga byte then converted into bytes =>
# memory_into_giga_bytes = float(input("please enter the size of the memory into giga bytes is = "))
# print("the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes")
# memory_into_bytes = memory_into_giga_bytes * 1073741824 
# print("the size of the memory into bytes is = "+str(memory_into_bytes)+" bytes")

memory_into_giga_bytes = float(input("please enter the size of the memory into giga bytes is = "))
print("the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes")
if(memory_into_giga_bytes > 0) :
    memory_into_bytes = memory_into_giga_bytes * 1073741824 
    print("the size of the memory into bytes is = "+str(memory_into_bytes)+" , because the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes")
else :
    print("there is no size of the memory into bytes , because the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga_bytes")