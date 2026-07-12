from random import randint
unsorted_list = [randint(0,600)for i in range(2,100000)]
sorted_list = []
def sort(func_list,thing,min1,max1):
    if len(func_list) == 0:
        return func_list.insert(0,thing)
    elif len(func_list) != 0:

        combined = min1 + max1
        guessed = func_list[combined//2]
    if min1 == max1:
        return func_list.insert(min1, thing)
    elif thing > guessed and (len(func_list) == combined//2+1 or thing < func_list[(combined//2)+1]):
        return func_list.insert((combined//2)+1, thing)
    elif guessed > thing:
        return sort(func_list,thing,min1,(combined//2))
    elif guessed < thing:
        return sort(func_list, thing,(combined//2)+1, max1)
    else:
        return func_list.insert(combined//2, thing)
def real_sort():
    while True:
        max2 = len(sorted_list)
        maxed = len(sorted_list)-1
        sort(sorted_list,unsorted_list.pop(),0,max2)
        if sorted(sorted_list) != sorted_list:
            break
        if len(unsorted_list) ==0:
            break
real_sort()
print(sorted_list)