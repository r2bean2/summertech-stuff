from random import *
import os
if not os.path.exists("index.txt"):
    with open("index.txt", "w") as file:
        file.write("1")
    index=1
else:
    with open("index.txt", "r") as file:
        index=int(file.read())
print(index)
old_index= index-1
file_path="evolve"+str(index)+".py"
vaild_charecters = [ chr(i) for i in range(32, 127)]
print(vaild_charecters)
char_add = vaild_charecters.pop(randint(0,len(vaild_charecters)))
print(char_add)
with open("evolve" + str(old_index) + ".py", "r") as file:
    py_file=file.read()
cut_point=randint(0,len(py_file))
py_file = py_file[:cut_point] + char_add + py_file[cut_point:]
print(py_file)
with open("index.txt", "w") as file:
    file.write(str(index + 1 ))