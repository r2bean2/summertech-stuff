num_to_count =int(input("number: "))
def calc(conter,calced_num):
    calced_num = calced_num * conter
    conter -=1
    if conter != 0:
        return calc(conter,calced_num)
    else:
        return calced_num
print(calc(num_to_count,1))
