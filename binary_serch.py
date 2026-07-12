test_list = [1,2,3,4,5,6,7,8,9,10]
real_sort()
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
print(serch(test_list, int(input("num to serch ")), 0, (len(test_list))-1))