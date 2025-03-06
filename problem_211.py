# write a python program to get size of the memory into bytes , and then converted to giga bytes =>
# memory_into_bytes = int(input("please enter the size of the memory into bytes is = "))
# print("the size of the memory into bytes is = "+str(memory_into_bytes)+" bytes")
# memory_into_giga_bytes = memory_into_bytes / 1073741824 
# print("the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes")

memory_into_bytes = int(input("please enter the size of the memory into bytes is = "))
if(memory_into_bytes > 0) :
    memory_into_giga_bytes = memory_into_bytes / 1073741824 
    print("the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes , because your entered size of the memory into bytes is = "+str(memory_into_bytes)+" bytes")
else :
    print("there is no size of the memory into giga bytes , because your entered size of the memory into bytes is = "+str(memory_into_bytes)+" bytes")