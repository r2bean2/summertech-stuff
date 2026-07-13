from fast_sort import sort
from random import randint
list_to_sort = [randint(0,1000000)for i in range(2,1000000)]
print(list_to_sort)
test_list = sort(list_to_sort)
print(test_list)
def serch(func_list,thing,min,max):
    if min == max:
        if func_list[min] == thing:
            return min
        else:
            return "failed"
    if min > max:
        return "failed"
    combined = min + max 
    guessed = func_list[combined//2] 
    if guessed > thing:
        return serch(func_list,thing,min,(combined//2)-1)
    elif guessed < thing:
        return serch(func_list, thing, (combined//2)+1, max)
    else:
        return combined//2
nums_index = serch(test_list, int(input("num to serch ")), 0, (len(test_list))-1)
print(nums_index)
print(test_list[nums_index])