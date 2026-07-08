def recursion_func(num):
    num = int(num)
    if num == 0:
        return 1
    else:
        return num*recursion_func(num-1)
print(recursion_func(input("number: ")))