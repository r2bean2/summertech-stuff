from random import randint
list_to_sort = [randint(0,1000000)for i in range(2,100000000)]
def sort(unsorted_list): 
    if len(unsorted_list) == 2:
        num1 = unsorted_list.pop()
        num2 = unsorted_list.pop()
        if num1 >= num2:
            unsorted_list.append(num2)
            unsorted_list.append(num1)
        elif num1 < num2:
            unsorted_list.append(num1)
            unsorted_list.append(num2)
        else:
            print("somthings off")
        return unsorted_list
    elif len(unsorted_list) == 1 or len(unsorted_list)==0:
        return unsorted_list
    else:
        pivote = unsorted_list[0]
        larger_list = []
        smaller_list = []
        equall_list = []
        for i in unsorted_list:
            if i > pivote:
                larger_list.append(i)
            elif i < pivote:
                smaller_list.append(i)
            elif i == pivote:
                equall_list.append(i)
            else:
                print("somthings off")
        return sort(smaller_list) + equall_list + (sort(larger_list))
print(list_to_sort)
sorted_list = sort(list_to_sort)
if sorted(sorted_list) == sorted_list:
    print(sorted_list)
else:
    print("sort did not work")